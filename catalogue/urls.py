from django.urls import path
from .views import TacheListView, TacheCreateView, TacheUpdateView, TacheDeleteView

urlpatterns = [
    path('', TacheListView.as_view(), name='liste'),
    path('ajouter/', TacheCreateView.as_view(), name='ajouter'),
    path('modifier/<int:pk>/', TacheUpdateView.as_view(), name='modifier'),
    path('supprimer/<int:pk>/', TacheDeleteView.as_view(), name='supprimer'),
]