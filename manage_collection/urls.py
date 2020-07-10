from .views import CollectionCreateView,CollectionDeleteView,CollectionDetailView,CollectionListView,CollectionUpdateView
from django.urls import path

urlpatterns = [
    path('create', CollectionCreateView.as_view()),
    path('list', CollectionListView.as_view()),
    path('detail/<int:pk>',CollectionDetailView.as_view()),
    path('update/<int:pk>',CollectionUpdateView.as_view()),
    path('delete/<int:pk>',CollectionDeleteView.as_view()),
]

