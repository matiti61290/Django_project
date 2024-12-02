import pytest
from django.urls import reverse 
from django.test import Client
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur
from django.utils import timezone
from datetime import timedelta
from bibliothecaire.forms import CreationMembre


# affichage liste media
@pytest.mark.django_db
def test_listemedia_view():
    client = Client()

    Livre.objects.create(titre='Livre Test', auteur='Auteur Test')
    Dvd.objects.create(titre='DVD Test', réalisateur='Réalisateur Test')
    Cd.objects.create(titre='CD Test', artiste='Artiste Test')
    JeuDePlateau.objects.create(nom='Jeu Test', éditeur='Éditeur Test')

    response = client.get(reverse('liste_media'))

    assert response.status_code == 200
    assert 'items/lists.html' in [template.name for template in response.templates]
    assert len(response.context['livres']) == 1
    assert len(response.context['dvds']) == 1
    assert len(response.context['cds']) == 1
    assert len(response.context['jeux']) == 1

# ajout media
@pytest.mark.django_db
def test_ajoutmedia_view_get():
    client = Client()
    response = client.get(reverse('ajout_media'))
    data = { 'Livre_form': '', 'nameLivre': 'Test Livre', 'auteur': 'Auteur Test' }
    response = client.post(reverse('ajout_media'), data=data)

    assert response.status_code == 302
    assert Livre.objects.filter(name='Test Livre').exists()

@pytest.mark.django_db
def test_ajoutmedia_view_post_dvd():
    client = Client()
    data = { 'DVD_form': '', 'nameDVD': 'Test DVD', 'realisateur': 'Réalisateur Test' }
    response = client.post(reverse('ajout_media'), data=data)

    assert response.status_code == 302
    assert Dvd.objects.filter(name='Test DVD').exists()

@pytest.mark.django_db
def test_ajoutmedia_view_post_cd():
    client = Client()
    data = { 'CD_form': '', 'nameCD': 'Test CD', 'artiste': 'Artiste Test' }
    response = client.post(reverse('ajout_media'), data=data)

    assert response.status_code == 302
    assert Cd.objects.filter(name='Test CD').exists()

@pytest.mark.django_db
def test_ajoutmedia_view_post_jeu():
    client = Client()
    data = { 'JeuDePlateau_form': '', 'name': 'Test Jeu', 'createur': 'Créateur Test' }
    response = client.post(reverse('ajout_media'), data=data)

    assert response.status_code == 302
    assert JeuDePlateau.objects.filter(name='Test Jeu').exists()

# Emprunt d'un media avec pour exemple un livre

@pytest.mark.django_db
def test_emprunt_livre_view_post():
    client = Client()

    emprunteur = Emprunteur.objects.create(name='Test Emprunteur', NombreEmprunt=0, EmpruntPossible=True)

    livre = Livre.objects.create(name='Test Livre', auteur='Auteur Test', disponible=True)

    data = {
        'emprunteur': emprunteur.id
    }
    response = client.post(reverse('emprunt_livre', args=[livre.id]), data=data)
    assert response.status_code == 302
    livre.refresh_from_db()
    emprunteur.refresh_from_db()
    assert not livre.disponible
    assert livre.emprunteur == emprunteur
    assert emprunteur.NombreEmprunt == 1

    emprunteur.NombreEmprunt = 3
    emprunteur.save()
    response = client.post(reverse('emprunt_livre', args=[livre.id]), data=data)
    assert response.status_code == 200
    assert 'items/emprunt/erreur.html' in [template.name for template in response.templates]

    livre2 = Livre.objects.create(name='Test Livre 2', auteur='Auteur Test 2', disponible=False, emprunteur=emprunteur, dateEmprunt=timezone.now() - timedelta(days=8))
    response = client.post(reverse('emprunt_livre', args=[livre2.id]), data=data)
    assert response.status_code == 200
    assert 'items/emprunt/erreur.html' in [template.name for template in response.templates]

@pytest.mark.django_db
def test_emprunt_livre_view_get():
    client = Client()
    livre = Livre.objects.create(name='Test Livre', auteur='Auteur Test', disponible=True)
    response = client.get(reverse('emprunt_livre', args=[livre.id]))

    assert response.status_code == 200
    assert 'items/emprunt/emprunt_livre.html' in [template.name for template in response.templates]
    assert 'emprunt_livre' in response.context

# Retour d'un media avec pour exemple un livre

@pytest.mark.django_db
def test_retour_livre_view():
    client = Client()

    emprunteur = Emprunteur.objects.create(name='Test Emprunteur', NombreEmprunt=1, EmpruntPossible=True)
    livre = Livre.objects.create(name='Test Livre', auteur='Auteur Test', disponible=False, emprunteur=emprunteur)

    response = client.get(reverse('retourLivre', args=[livre.id]))
    assert response.status_code == 302

    livre.refresh_from_db()
    emprunteur.refresh_from_db()

    assert livre.disponible
    assert livre.emprunteur is None
    assert emprunteur.NombreEmprunt == 0

@pytest.mark.django_db
def test_retour_livre_view_without_emprunteur():
    client = Client()

    livre = Livre.objects.create(name='Test Livre', auteur='Auteur Test', disponible=True, emprunteur=None)

    response = client.get(reverse('retour_livre', args=[livre.id]))
    assert response.status_code == 302  # Redirection après le retour du livre

    livre.refresh_from_db()

    assert livre.disponible
    assert livre.emprunteur is None

# Ajout d'un membre

@pytest.mark.django_db
def test_ajoutmembre_view_get():
    client = Client()
    response = client.get(reverse('ajout_membre')) 

    assert response.status_code == 200
    assert 'emprunteurs/ajout_emprunteur.html' in [template.name for template in response.templates]
    assert 'form_membre' in response.context
    assert isinstance(response.context['form_membre'], CreationMembre)

@pytest.mark.django_db
def test_ajoutmembre_view_post():
    client = Client()

    data = {
        'name': 'Test',
        'surname': 'User',
    }
    
    response = client.post(reverse('ajout_membre'), data=data)
    
    assert response.status_code == 302
    assert Emprunteur.objects.filter(name='Test User').exists()

    emprunteur = Emprunteur.objects.get(name='Test User')
    assert emprunteur.NombreEmprunt == 0

# Suppression d'un membre

@pytest.mark.django_db
def test_supprimer_membre_view():
    client = Client()

    emprunteur = Emprunteur.objects.create(name='Test Emprunteur', NombreEmprunt=1, EmpruntPossible=True)

    assert Emprunteur.objects.filter(pk=emprunteur.pk).exists()

    response = client.get(reverse('supprimer_membre', args=[emprunteur.pk]))
    
    assert response.status_code == 302 

    assert not Emprunteur.objects.filter(pk=emprunteur.pk).exists()
