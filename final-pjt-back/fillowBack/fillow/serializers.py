from rest_framework import serializers
from .models import MovieLocation, Movie, Genre   
from rest_framework.exceptions import ValidationError


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
    id = serializers.IntegerField(source='movie_id')
    vote_average = serializers.FloatField(source='vote_avg')
    class Meta:
        model = Movie
        fields = ('id','title','release_date','popularity','vote_count','vote_average','overview','poster_path','adult','backdrop_path','original_language','original_title','revenue','runtime','tagline',)
        # exclude = ('genres', )
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except:
            raise ValidationError('unique error')