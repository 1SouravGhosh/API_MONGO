import manage_command
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('command/',include('manage_command.urls')),
    path('collection/',include('manage_collection.urls')),
    path('schedule/',include('manage_schedule.urls')),
]
