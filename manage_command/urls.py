from .views import CommandCreateView, CommandDetailView,CommandListView,CommandUpdateView,CommandDeleteView
from django.urls import path

urlpatterns = [
    path('create', CommandCreateView.as_view()),
    path('list', CommandListView.as_view()),
    path('detail/<int:pk>',CommandDetailView.as_view()),
    path('update/<int:pk>',CommandUpdateView.as_view()),
    path('delete/<int:pk>',CommandDeleteView.as_view()),
]
