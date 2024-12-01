from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('listes/', views.listemedia, name='listes_media'),
    path('emprunteurs/', views.listeemprunteur, name='listeEmprunteurs'),
    path('ajoutmedia/', views.ajoutmedia, name='ajout_media'),
    path('ajoutmembre/', views.ajoutmembre, name='ajout_membre'),
    path('supprimer_membre/<int:id>/', views.supprimer_membre, name='supprimer_membre'),
    path('listes/emprunt_livre/<int:livre_id>/', views.empruntLivre, name='emprunt_livre'),
    path('retourlivre/<int:livre_id>/', views.retourLivre, name='retour_livre'),
    path('listes/emprunt_dvd/<int:dvd_id>/', views.empruntDvd, name='emprunt_dvd'),
    path('retourdvd/<int:dvd_id>/', views.retourDvd, name='retour_dvd'),
    path('listes/emprunt_cd/<int:cd_id>/', views.empruntCd, name="emprunt_cd"),
    path('retourcd/<int:cd_id>/', views.retourCd, name='retour_cd')
]