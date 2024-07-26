from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Job, ApplyJob
from .forms import CreationJobForm, UpdateJobForm

# Create your views here.
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreationJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New job has been created')
                return redirect('dashboard:dashboard')
            else:
                messages.warning(request, 'something when wrong')
                return redirect('create-job')
        else:
            form = CreationJobForm()
            context = {'form': form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard:dashboard')
    
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'You job info has been updated')
            return redirect('dashboard:dashboard')
        else:
            messages.warning(request, 'something when wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)
    
def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)


def apply_to_job(request, pk):
    if request.user.is_authenticated and request.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
           messages.warning(request, 'Permission Denied')
           return redirect('dashboard:dashboard') 
        else:
            ApplyJob.objects.create(
                job=job,
                user = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have successfully applied! Please see dashboard')
            return redirect('dashboard:dashboard')
    else:
        messages.info(request, 'Please log in to continue')
        return redirect('user:login')
    
    
def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = ApplyJob.objects.all()
    context = {'job':job, 'applicants':applicants}
    return render(request, 'job/all_applicants.html', context)
                
