from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("", views.apiOverview, name="api-overview"),

  path("movies/", views.movieList, name="movies"),
  path("movie/<str:id>/", views.movieDetail, name="movie-detail"),
  path("create-movie/", views.movieCreate, name="create-movie"),
  path("update-movie/<str:id>", views.movieUpdate, name="update-movie"),
  path("delete-movie/<str:id>", views.movieDelete, name="delete-movie"),

  path("genres/", views.genresList, name="genres"),
  path("genre/<str:id>/", views.genreDetail, name="genre-detail"),
  path("create-genre/", views.createGenre, name="create-genre"),
  path("update-genre/<str:id>", views.updateGenre, name="update-genre"),
  path("delete-genre/<str:id>", views.deleteGenre, name="delete-genre"),
]
