from rest_framework import serializers
from.models import Post

class PostSerializer(serializers.ModelSerializer):
    data = serializers.DateTimeField(input_formats=['%d-%m-%Y',])

    class Meta:
        model = Post