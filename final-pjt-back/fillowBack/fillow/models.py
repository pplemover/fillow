from django.db import models
from django.conf import settings

# Create your models here.
# 07 08 참고
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)  #
    release_date = models.DateField()  #
    popularity = models.FloatField()  #
    vote_count = models.IntegerField()  #
    vote_avg = models.FloatField()
    # 평균평점 vote_avg = models.DecimalField(max_digits=5, decimal_places=3) 
    overview = models.TextField()  #
    poster_path = models.CharField(max_length=200)  #
    genres = models.ManyToManyField(Genre)  #
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    tagline = models.CharField(max_length=100)


# ============================================================================================================
class MovieLocation(models.Model):
    # title = models.CharField(max_length=50)        # 영화 제목 (TMDB에서 받아올거)
    tmdb_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # tmdb_id = models.IntegerField()                # tmdb_id
    location_name = models.CharField(max_length=50)  # 장소 이름
    latitude = models.DecimalField(max_digits=15, decimal_places=6)  # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=6) # 경도
    location_country = models.CharField(max_length=20) # 장소가 위치한 나라 이름
    youtube_url = models.URLField(max_length=300)    # 유튜브 동영상 링크
    location_photo_url = models.URLField(max_length=300) # 장소 사진 url
    location_description = models.TextField()        # 장소 설명
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
