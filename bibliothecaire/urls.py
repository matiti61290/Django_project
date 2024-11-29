from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('listes/', views.listemedia, name='listes_media'),
    path('emprunteurs/', views.listeemprunteur, name='listeEmprunteurs'),
    path('ajoutmedia/', views.ajoutmedia),
    path('ajoutmembre/', views.ajoutmembre),
    path('supprimer_membre/<int:id>/', views.supprimer_membre, name='supprimer_membre'),
    path('listes/emprunt/<int:livre_id>/', views.empruntLivre, name='emprunt_livre'),
    path('retour/<int:livre_id>/', views.retourLivre, name='retour_livre')
]