# mongo_app/serializers.py
from rest_framework import serializers
from .models import Pelicula
from bson.objectid import ObjectId
from rest_framework import serializers

# mongo_app/serializers.py
# (Asegúrate de que la clase ObjectIdField esté definida arriba)

class PeliculaSerializer(serializers.ModelSerializer):
    # Usa el campo personalizado para el ID
   # id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = Pelicula
        # Lista explícitamente los campos, incluyendo 'id'
        fields = '__all__'