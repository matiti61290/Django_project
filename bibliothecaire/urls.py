from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('listes/', views.listemedia),
    path('emprunteurs/', views.listeemprunteur),
    path('ajoutmedia/', views.ajoutmedia)
]