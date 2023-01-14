from rest_framework import serializers
from .models import Astartes

class AstartesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Astartes
        fields ='__all__'