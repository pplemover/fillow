from rest_framework import serializers
from .models import MovieLocation, Movie, Genre   
 
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLocation
        fields = '__all__'
        

        
class MovieDetailSerializer(serializers.ModelSerializer):
    movielocation_set = MovieLocationSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('movielocation_set',)

class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('genres', )