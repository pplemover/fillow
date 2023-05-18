from rest_framework import serializers
from .models import MovieLocation

class MovieLocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieLocation
        fields = '__all__'
        