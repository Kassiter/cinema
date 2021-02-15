from django.contrib import admin
from api.models import Movie, Genre, Comment, User

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(User)

# Register your models here.
