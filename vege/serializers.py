from rest_framework import serializers
from .models import Receipe

class RecipeSerializer(serializers.ModelSerializer):
     user = serializers.RelatedField(read_only=True)
     receipe_image = serializers.ImageField(required=False, allow_null=True)
     class Meta:
          model = Receipe
          fields = "__all__"