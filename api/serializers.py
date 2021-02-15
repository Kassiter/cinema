from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
import os

class MovieSerializer(serializers.ModelSerializer):
  video = serializers.SerializerMethodField()
  cover = serializers.SerializerMethodField()

  def get_video(self, obj):
    return f'{os.getenv("APP_HOST")}{obj.video.url}'

  def get_cover(self, obj):
    return f'{os.getenv("APP_HOST")}{obj.cover.url}'

  class Meta:
    model = Movie
    fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  avatar = serializers.SerializerMethodField()

  def get_avatar(self, obj):
    return f'{os.getenv("APP_HOST")}{obj.avatar.url}'
  class Meta:
    model = User
    exclude = ('password', )

class RegistrationSerializer(serializers.ModelSerializer):

    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """
    Authenticates an existing user.
    Email and password are required.
    Returns a JSON web token.
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates user data.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
        }

class MovieRatingSerializer(serializers.ModelSerializer):

  def validate(self, data):
    movie = data.get('movie', None)
    user = data.get('user', None)
    rating = data.get('rating', None)
    existing_rating = MovieRating.objects.filter(movie_id=movie, user_id=user).first()

    if movie is None:
        raise serializers.ValidationError(
            'Movie id is required.'
        )

    if rating is None:
        raise serializers.ValidationError(
            'A rating is required.'
        )
    
    if existing_rating:
        raise serializers.ValidationError(
            'Such rating already exists.'
        )

    return data
  class Meta:
    model = MovieRating
    fields = '__all__'
    validators = []

class CommentSerializer(serializers.ModelSerializer):

  def validate(self, data):
    movie = data.get('movie', None)
    content = data.get('content', None)

    if movie is None:
        raise serializers.ValidationError(
            'Movie id is required.'
        )

    if content is None:
        raise serializers.ValidationError(
            'A content is required.'
        )

    return data
  class Meta:
    model = Comment
    fields = '__all__'
    validators = []
