from django import forms
from bibliothecaire.models import Emprunteur

class CreationLivre(forms.Form):
    nameLivre = forms.CharField(required=True, label='Nom livre')
    auteur = forms.CharField(required=True, label='Auteur')

class CreationDvd(forms.Form):
    nameDVD = forms.CharField(required=True, label='Nom DVD')
    realisateur = forms.CharField(required=True, label='Réalisateur')

class CreationCd(forms.Form):
    nameCD = forms.CharField(required=True, label='Nom CD')
    artiste = forms.CharField(required=True, label='Artiste')

class CreationJeuDePlateau(forms.Form):
    name = forms.CharField(required=True, label='Nom du jeu')
    createur = forms.CharField(required=True, label='Créateur')

class CreationMembre(forms.Form):
    name = forms.CharField(required=True, label='Nom du membre')

class EmpruntLivre(forms.Form):
    disponible = forms.BooleanField(required=True)
    emprunteur = forms.ModelChoiceField(
        queryset=Emprunteur.objects.all(),
        label="Sélectionnez un membre"
    )

class EmpruntDvd(forms.Form):
    disponible = forms.BooleanField(required=True)
    emprunteur = forms.ModelChoiceField(
        queryset=Emprunteur.objects.all(),
        label="Sélectionnez un membre"
    )

class EmpruntCd(forms.Form):
    disponible = forms.BooleanField(required=True)
    emprunteur = forms.ModelChoiceField(
        queryset=Emprunteur.objects.all(),
        label="Sélectionnez un membre"
    )