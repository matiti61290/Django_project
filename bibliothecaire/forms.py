from django import forms

class CreationLivre(forms.Form):
    nameLivre = forms.CharField(required=True)
    auteur = forms.CharField(required=True)

class CreationDvd(forms.Form):
    nameDVD = forms.CharField(required=True)
    realisateur = forms.CharField(required=True)

class CreationCd(forms.Form):
    nameCD = forms.CharField(required=True)
    artiste = forms.CharField(required=True)

class CreationJeuDePlateau(forms.Form):
    name = forms.CharField(required=True)
    createur = forms.CharField(required=True)

class CreationMembre(forms.Form):
    name = forms.CharField(required=True)
    # prenom = forms.CharField(required=True)