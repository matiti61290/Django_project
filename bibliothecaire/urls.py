from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('listes/', views.listelivres),
    path('emprunteurs/', views.listeemprunteur)
]