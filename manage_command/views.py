from rest_framework.generics import (CreateAPIView,ListAPIView,DestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView,UpdateAPIView,RetrieveAPIView)
from .models import Command
from .serializer import CommandSerializer,CommandModifySerializer

class CommandCreateView(CreateAPIView):
    model = Command
    serializer_class = CommandModifySerializer


class CommandListView(ListAPIView):
    model = Command
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.all()


class CommandDetailView(RetrieveAPIView):
    model = Command
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.all()
    

class CommandUpdateView(RetrieveUpdateAPIView):
    model = Command
    serializer_class = CommandModifySerializer

    def get_queryset(self):
        return Command.objects.all()
       

class CommandDeleteView(RetrieveDestroyAPIView):
    model = Command
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.all()
    


    


