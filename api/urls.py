from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
  path("", views.apiOverview, name="api-overview"),

  path("movies/", MoviesAPIView.index, name="movies"),
  path("movies/<str:id>/", MoviesAPIView.show, name="movie-detail"),
  path("movies/new/", MoviesAPIView.create, name="create-movie"),
  path("movies/<str:id>/edit/", MoviesAPIView.update, name="update-movie"),
  path("movies/<str:id>/delete/", MoviesAPIView.destroy, name="delete-movie"),

  path("genres/", GenresAPIView.index, name="genres"),
  path("genres/<str:id>/", GenresAPIView.show, name="genre-detail"),
  path("genres/new/", GenresAPIView.create, name="create-genre"),
  path("genres/<str:id>/edit/", GenresAPIView.update, name="update-genre"),
  path("genres/<str:id>/delete/", GenresAPIView.destroy, name="delete-genre"),

  path("movie_ratings/", MovieRatingsAPIView.index, name="movie_ratings"),
  path("movie_ratings/<str:id>/",MovieRatingsAPIView.show, name="movie_rating-detail"),
  path("movie_ratings/new",MovieRatingsAPIView.create, name="create-movie_rating"),
  path("movie_ratings/<str:id>/edit",MovieRatingsAPIView.update, name="update-movie_rating"),
  path("movie_ratings/<str:id>/delete",MovieRatingsAPIView.destroy, name="delete-movie_rating"),

  path("users/<str:id>/", UsersAPIView.show, name="user-detail"),

  re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
  re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]
