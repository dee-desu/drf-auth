from django.urls import path 
from .views import AstartesListCreateView,AstartesDetailView
urlpatterns = [
    path('',AstartesListCreateView.as_view(),name='astartes_list_create'),
    path('<int:pk>/',AstartesDetailView.as_view(),name='astartes_detail'),
]