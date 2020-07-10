from rest_framework.serializers import ModelSerializer
from .models import Collection

class CollectionSerializer(ModelSerializer):
    class Meta():
        model = Collection
        fields = ('id','name','schedule','commands')
        view_only_field = ('commands',)
        depth=2

class CollectionModifySerializer(ModelSerializer):
    class Meta():
        model = Collection
        fields = ('id','name','schedule','commands')
        
        