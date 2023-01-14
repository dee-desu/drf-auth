from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Astartes
from .serializers import AstartesSerializer
from .permissions import OwnerOnly

class AstartesListCreateView(ListCreateAPIView):
    queryset= Astartes.objects.all()
    serializer_class=AstartesSerializer


class AstartesDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Astartes.objects.all()
    serializer_class=AstartesSerializer
    permission_classes=[OwnerOnly]
    