from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur
from bibliothecaire.forms import CreationLivre

#Liste des items
def listelivres(request):
    livres = Livre.objects.all()
    return render(request, 'items/lists.html',
                  {'livres': livres})

def listedvd(request):
    dvds = Dvd.objects.all()
    return render(request, 'items/lists.html',
                  {'dvds': dvds})

def listecd(request):
    cds = Cd.objects.all()
    return render(request, 'items/lists.html',
                  {'cds': cds})

def listjeuplateau(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'items/lists.html',
                  {'jeux' : jeux})

# Ajout media

def ajoutlivre(request):
    if request.method == "POST":
        creationlivre = CreationLivre(request.POST)
        if creationlivre.is_valid():
            livre = Livre()
            livre.name = creationlivre.cleaned_data['name']
            livre.auteur = creationlivre.cleaned_data['auteur']
            livre.disponible = True
            livre.save()
            livres = Livre.objects.all()
            return render(request, 'items/lists.html',
                          {'livres': livres})
    else:
        creationlivre = CreationLivre()
        return render(request, 'items/ajout_media.html',
                        {'creationLivre':creationlivre})

# liste des membres
def listeemprunteur(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'emprunteurs/list.html',
                  {'emprunteurs': emprunteurs})