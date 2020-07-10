from rest_framework.serializers import ModelSerializer
from .models import Schedule

class ScheduleSerializer(ModelSerializer):
    class Meta():
        model = Schedule
        fields = ('id','name','start_date','end_date','start_time','end_time','collections')
        read_only_fields = ('collections',)
        # depth = 2
