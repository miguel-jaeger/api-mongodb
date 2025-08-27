# mongo_app/views.py
from rest_framework import viewsets
from .models import Pelicula
from .serializers import PeliculaSerializer

        
class PeliculaViewSet(viewsets.ModelViewSet):
    # This ensures the ViewSet fetches data from the database
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer