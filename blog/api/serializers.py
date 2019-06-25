from rest_framework import serializers
from blog.models import *
from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer,SerializerMethodField

class BlogSerializer(ModelSerializer):
    topic = serializers.CharField(source="Topic.subject",read_only=True)

    class Meta:
        model = Blog
        fields = [
            'title',
            'topic',
            'updated_at',
            'created_by',
            'link1',    
            'Blog_Text',
        ]
   
class LatestSerializer(ModelSerializer):
    #creater = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #creater = SerializerMethodField()

    class Meta:
        model = latest
        fields =[
            "slug",
            "id",
            #"creater",    
            "category",
            "topic",
            "title",
            "last_update",
            "link2",
            "content",

                ]
    #def get_user(self,obj):
       # return str(obj.creater.username)
