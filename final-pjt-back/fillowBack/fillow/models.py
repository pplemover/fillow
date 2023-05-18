from django.db import models

# Create your models here.
class MovieLocation(models.Model):
    # title = models.CharField(max_length=50)          # 영화 제목 (TMDB에서 받아올거)
    tmdb_id = models.IntegerField()                  # tmdb_id
    location_name = models.CharField(max_length=50)  # 장소 이름
    latitude = models.DecimalField(max_digits=15, decimal_places=6)  # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=6) # 경도
    location_country = models.CharField(max_length=20) # 장소가 위치한 나라 이름
    youtube_url = models.URLField(max_length=300)    # 유튜브 동영상 링크
    location_photo_url = models.URLField(max_length=300) # 장소 사진 url
    location_description = models.TextField()        # 장소 설명
    
    # vote_average = models.DecimalField(max_digits=5, decimal_places=3)      # 평균 평점
    # 장르
    # 성인영화 여부
    # 연도
    # 감독
    # 줄거리
    # 포스터 url
    # 배경 url
    # 원제목
    
    
