from rest_framework import serializers
from .models import House


class HouserSerializer(serializers.ModelSerializer):
    # members_count = serializers.IntegerField(read_only=True)
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True,view_name='profile-detail')
    customers= serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')

    class Meta:
        model = House
        fields = ['url','id','image','name','created_on','customers','description','points',
        'completed_tasks_count','members','notcompleted_tasks_count']

        read_only_fields = ['points','completed_tasks_count','notcompleted_tasks_count']