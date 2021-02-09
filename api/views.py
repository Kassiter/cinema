from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import *
from .models import Movie, Genre, User

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/movie-list/'
  }

  return Response(api_urls)
# -----------------------USERS-----------------------

class UsersAPIView(APIView):
  authentication_classes = [AllowAny]

  @api_view(['GET'])
  def show(request, id):
    user = User.objects.get(id = id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# ---------------------- MOVIES ---------------------
class MoviesAPIView(APIView):
  @api_view(['GET'])
  def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

  @api_view(['GET'])
  def show(request, id):
    movie = Movie.objects.get(id = id)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

  @api_view(['POST'])
  def create(request):
    serializer = MovieSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)

  @api_view(['PUT', 'PATCH'])
  def update(request, id):
    movie = Movie.objects.get(id = id)
    serializer = MovieSerializer(instance = movie, data = request.data)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)

  @api_view(['DELETE'])
  def destroy(request, id):
    movie = Movie.objects.get(id = id).delete()

    return Response('Deleted')

# ---------------------- Genres ---------------------
class GenresAPIView(APIView):
  @api_view(['GET'])
  def index(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many = True)
    
    return Response(serializer.data)

  @api_view(['GET'])
  def show(request, id):
    genre = Genre.objects.get(id = id)
    serializer = GenreSerializer(genre, many=False)

    return Response(serializer.data)

  @api_view(['POST'])
  def create(request):
    serializer = GenreSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)

  @api_view(['PUT', 'PATCH'])
  def update(request, id):
    genre = Genre.objects.get(id = id)
    serializer = GenreSerializer(instance = genre, data = request.data)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)

  @api_view(['DELETE'])
  def destroy(request, id):
    genre = Genre.objects.get(id = id).delete()

    return Response(genre)

# ---------------------- Movie Ratings ---------------------
class MovieRatingsAPIView(APIView):
  # permission_classes = [AllowAny]

  @api_view(['GET'])
  def index(request):
    movie_ratings = MovieRating.objects.all()
    serializer = MovieRatingSerializer(movie_ratings, many = True)
    
    return Response(serializer.data)

  @api_view(['GET'])
  def show(request, id):
    movie_rating = MovieRating.objects.get(id = id)
    serializer = MovieRatingSerializer(movie_rating, many=False)

    return Response(serializer.data)

  @api_view(['POST'])
  def create(request):
    request.data['user'] = request.user.id
    serializer = MovieRatingSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
      serializer.save()

    return Response(serializer.data)

  @api_view(['PUT', 'PATCH'])
  def update(request, id):
    movie_rating = MovieRating.objects.get(id = id)
    serializer = MovieRatingSerializer(instance = movie_rating, data = request.data)

    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)

  @api_view(['DELETE'])
  def destroy(request, id):
    movie_rating = MovieRating.objects.get(id = id).delete()

    return Response(genre)


# -------------------------AUTH-----------------
class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )

class LoginAPIView(APIView):
  """
  Logs in an existing user.
  """
  permission_classes = [AllowAny]
  serializer_class = LoginSerializer

  def post(self, request):
      """
      Checks is user exists.
      Email and password are required.
      Returns a JSON web token.
      """
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)

      return Response(serializer.data, status=status.HTTP_200_OK)