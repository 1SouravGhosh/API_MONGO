from rest_framework.serializers import ModelSerializer
from .models import Command

class CommandSerializer(ModelSerializer):
    class Meta():
        model = Command
        fields = ('id','command','collection')
        depth = 2

class CommandModifySerializer(ModelSerializer):
    class Meta():
        model = Command
        fields = ('id','command','collection')
       
