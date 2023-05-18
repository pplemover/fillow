from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieLocation
from .serializers import MovieLocationSerializer

from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    # get method는 모든 목록을 달라고 할때
    if request.method == "GET":
        movies = get_list_or_404(MovieLocation)
        serializer = MovieLocationSerializer(movies, many=True)
        return Response(serializer.data)
    
    # post method는 영화 데이터를 넣을때
    if request.method == "POST":
        serializer = MovieLocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
