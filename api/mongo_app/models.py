from django.db import models
from djongo import models as djongo_models

# No uses models.Model, usa djongo_models.Model
# Esto es crucial para trabajar directamente con colecciones de MongoDB
class Pelicula(djongo_models.Model):
    # Campos que coinciden con los de tu documento en la imagen
     # This explicit field definition is crucial
    _id = djongo_models.ObjectIdField(primary_key=True)
    poster = models.TextField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    genres = djongo_models.JSONField(blank=True, null=True)
    languages = djongo_models.JSONField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    cast = djongo_models.JSONField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True) # Changed to CharField
    imdb = djongo_models.JSONField(blank=True, null=True)
    directors = djongo_models.JSONField(blank=True, null=True)
    writers = djongo_models.JSONField(blank=True, null=True)
    awards = djongo_models.JSONField(blank=True, null=True)
    countries = djongo_models.JSONField(blank=True, null=True)
    
    class Meta:
        # Esto le indica a Django que se conecte a la colección 'movies'
        # del mismo nombre en MongoDB.
        db_table = 'movies'

    def __str__(self):
        return self.title