from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'M_id',
            'M_pw',
        )
        model = Post
