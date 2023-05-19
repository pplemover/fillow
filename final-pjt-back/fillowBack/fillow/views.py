from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieLocation, Movie
from .serializers import MovieLocationSerializer, MovieSerializer, MovieDetailSerializer, MovieCreateSerializer

from rest_framework import status
from django.http import QueryDict

#=========================요청==============
import requests


TMDB_API_KEY = '6aee34be99bb1d1b3fa358b709332b7e'  # .env 파일에서 불러옴.

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def location_list(request):
    # get method는 모든 목록을 달라고 할때
    if request.method == "GET":
        movies = get_list_or_404(MovieLocation)
        serializer = MovieLocationSerializer(movies, many=True)
        return Response(serializer.data)
    
    # post method는 영화 데이터를 넣을때
    elif request.method == "POST":
        # =============영화 데이터 tmdb에 요청할거임 key 받아서
        # print(request.data)  # 쿼리딕 형태
        serializer = MovieLocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

@api_view(['PUT'])
def update_location(request, location_pk):
    location = MovieLocation.objects.get(pk=location_pk)
    if request.method == 'PUT':
        serializer = MovieLocationSerializer(location, data =request.data) # the ArticleSerializer is updated using the passed data 
        if serializer.is_valid(raise_exception=True): # After validation,
            serializer.save() # the updated article object is saved.
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_list(request):
    # get method는 모든 목록을 달라고 할때
    if request.method == "GET":
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        # print(request.GET.get('id'), '##############################')  # 아이디 받아옴
        movie_pk = request.GET.get('id')
        request_url = f"https://api.themoviedb.org/3/movie/{movie_pk}?api_key={TMDB_API_KEY}&language=ko-KR"
        movie = requests.get(request_url).json()
        

        genre_lst = [genre['id'] for genre in movie['genres']]
        mydict = {
            'movie_id': movie['id'],
            'title': movie['title'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
            'vote_avg': movie['vote_average'],
            'overview': movie['overview'],
            'poster_path': movie['poster_path'],
            # 'genres': {id:12, id:14},
            'vote_count': movie['vote_count'],
        }
        query_dict = QueryDict('', mutable=True)
        query_dict.update(mydict)
        serializer = MovieCreateSerializer(data=query_dict)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            cur_movie = Movie.objects.get(pk = movie_pk)
            for genre_id in genre_lst:
                cur_movie.genres.add(genre_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "GET":
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    