from rest_framework.generics import (CreateAPIView,ListAPIView, 
RetrieveDestroyAPIView, 
RetrieveUpdateAPIView,
RetrieveAPIView)
from .models import Collection
from .serializer import CollectionSerializer,CollectionModifySerializer



class CollectionCreateView(CreateAPIView):
    model = Collection
    serializer_class = CollectionModifySerializer


class CollectionListView(ListAPIView):
    model = Collection
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.all()


class CollectionDetailView(RetrieveAPIView):
    model = Collection
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.all()
    

class CollectionUpdateView(RetrieveUpdateAPIView):
    model = Collection
    serializer_class = CollectionModifySerializer

    def get_queryset(self):
        return Collection.objects.all()
       

class CollectionDeleteView(RetrieveDestroyAPIView):
    model = Collection
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.all()
    


    


