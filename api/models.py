from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Movie(models.Model):
  title = models.CharField(max_length=200)
  # release_date = models.DateField(auto_now=False, auto_now_add=False)
  video = models.FileField(null=True, verbose_name="")
  cover = models.ImageField(default='default.png', blank=True)
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
  genres = models.ManyToManyField('Genre')

  def __str__(self):
      return self.title

class Genre(models.Model):
  name = models.CharField(max_length=50)
  movies = models.ManyToManyField(Movie)

  def __str__(self):
      return self.name
