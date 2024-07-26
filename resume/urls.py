from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('update-resume/', views.update_resume, name='update-resume'),
    path('resume-details/', views.resume_details, name='resume-details'),
]
