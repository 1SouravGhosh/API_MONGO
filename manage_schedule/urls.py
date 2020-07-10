from .views import ScheduleCreateView,ScheduleDetailView,ScheduleListView,ScheduleUpdateView,ScheduleDeleteView
from django.urls import path


urlpatterns = [
    path('create', ScheduleCreateView.as_view()),
    path('list', ScheduleListView.as_view()),
    path('detail/<int:pk>',ScheduleDetailView.as_view()),
    path('update/<int:pk>',ScheduleUpdateView.as_view()),
    path('delete/<int:pk>',ScheduleDeleteView.as_view()),
]

