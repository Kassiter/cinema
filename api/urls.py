from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RegistrationAPIView, MoviesAPIView, GenresAPIView, LoginAPIView, UsersAPIView

urlpatterns = [
  path("", views.apiOverview, name="api-overview"),

  path("movies/", MoviesAPIView.index, name="movies"),
  path("movie/<str:id>/", MoviesAPIView.show, name="movie-detail"),
  path("create-movie/", MoviesAPIView.create, name="create-movie"),
  path("update-movie/<str:id>", MoviesAPIView.update, name="update-movie"),
  path("delete-movie/<str:id>", MoviesAPIView.destroy, name="delete-movie"),

  path("genres/", GenresAPIView.index, name="genres"),
  path("genre/<str:id>/", GenresAPIView.show, name="genre-detail"),
  path("create-genre/", GenresAPIView.create, name="create-genre"),
  path("update-genre/<str:id>", GenresAPIView.update, name="update-genre"),
  path("delete-genre/<str:id>", GenresAPIView.destroy, name="delete-genre"),

  path("user/<str:id>/", UsersAPIView.show, name="user-detail"),

  re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
  re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]
