from django.urls import path, include
from fillow import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('location/', views.location_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('updatelocation/<int:location_pk>/', views.update_location),
    
    # path('articles/<int:article_pk>/', views.article_detail),
    # path('articles/<int:article_pk>/comments/', views.comment_list),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
]