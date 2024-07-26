from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls', namespace='website')),
    path('accounts/', include('user.urls', namespace='user')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('company/', include('company.urls', namespace='company')),
    path('resume/', include('resume.urls', namespace='resume')),
    path('jobs/', include('job.urls', namespace='job')),
    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)