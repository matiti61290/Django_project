from django import forms

class CreationLivre(forms.Form):
    name = forms.CharField(required=True)
    auteur = forms.CharField(required=True)

class CreationDvd(forms.Form):
    name = forms.CharField(required=True)
    realisateur = forms.CharField(required=True)

class CreationCd(forms.Form):
    name = forms.CharField(required=True)
    artiste = forms.CharField(required=True)

class CreationJeuDePlateau(forms.Form):
    name = forms.CharField(required=True)
    createur = forms.CharField(required=True)