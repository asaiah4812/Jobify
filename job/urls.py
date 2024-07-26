from django.urls import path
from . import views

app_name = "job"

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('apply-to-jobs/<int:pk>/', views.apply_to_job, name='apply-to-jobs'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants')
]