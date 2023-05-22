from rest_framework import serializers
from .models import MovieLocation, Movie, Genre   


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLocation
        fields = '__all__'

        
class MovieDetailSerializer(serializers.ModelSerializer):
    movielocation_set = MovieLocationSerializer(many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('movielocation_set',)

class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('genres', )