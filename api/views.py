from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/movie-list/'
  }

  return Response(api_urls)

# ---------------------- MOVIES ---------------------

@api_view(['GET'])
def movieList(request):
  movies = Movie.objects.all()
  serializer = MovieSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def movieDetail(request, id):
  movie = Movie.objects.get(id = id)
  serializer = MovieSerializer(movie, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def movieCreate(request):
  serializer = MovieSerializer(data = request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['PUT'])
def movieUpdate(request, id):
  movie = Movie.objects.get(id = id)
  serializer = MovieSerializer(instance = movie, data = request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def movieDelete(request, id):
  movie = Movie.objects.get(id = id).delete()

  return Response('Deleted')

# ---------------------- Genres ---------------------

@api_view(['GET'])
def genresList(request):
  genres = Genre.objects.all()
  serializer = GenreSerializer(genres, many = True)
  
  return Response(serializer.data)

@api_view(['GET'])
def genreDetail(request, id):
  genre = Genre.objects.get(id = id)
  serializer = GenreSerializer(genre, many=False)

  return Response(serializer.data)

@api_view(['POST'])
def createGenre(request):
  serializer = GenreSerializer(data = request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['PUT'])
def updateGenre(request, id):
  genre = Genre.objects.get(id = id)
  serializer = GenreSerializer(instance = genre, data = request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def deleteGenre(request, id):
  genre = Genre.objects.get(id = id).delete()

  return Response(genre)
