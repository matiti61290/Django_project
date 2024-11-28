from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('listes/', views.listemedia),
    path('emprunteurs/', views.listeemprunteur, name='listeEmprunteurs'),
    path('ajoutmedia/', views.ajoutmedia),
    path('ajoutmembre', views.ajoutmembre),
    path('supprimer_membre/<int:id>/', views.supprimer_membre, name='supprimer_membre')
]