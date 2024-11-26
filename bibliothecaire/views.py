from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur

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

# liste des membres
def listeemprunteur(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'emprunteurs/list.html',
                  {'emprunteurs': emprunteurs})