from rest_framework import serializers
from .models import Simple_API

class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Simple_API
        fields=('name', 'description')

