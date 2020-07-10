from rest_framework.generics import (CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView)
from .models import Schedule
from .serializer import ScheduleSerializer

class ScheduleCreateView(CreateAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer


class ScheduleDetailView(RetrieveAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()


class ScheduleListView(ListAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()
    

class ScheduleUpdateView(RetrieveUpdateAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()


class ScheduleDeleteView(RetrieveDestroyAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()



