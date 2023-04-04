from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
  title=serializers.CharField(max_length=50)
  
  class Meta:
    model = Post
    fields = ["id", "title", "content", "created"]



# class PostSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField(max_length=200)
#   content = serializers.CharField()
#   created = serializers.DateTimeField(read_only=True)