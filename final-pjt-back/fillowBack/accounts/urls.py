
from django.urls import path, include
from . import views

urlpatterns = [
    path('userprofile/<int:user_pk>/', views.profile),
    path('follow/<int:user_pk>/', views.follow),
]
