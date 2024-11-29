from django.shortcuts import render, get_object_or_404
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur
from bibliothecaire.forms import CreationLivre, CreationCd, CreationDvd, CreationJeuDePlateau, CreationMembre, EmpruntLivre

def listemedia(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'items/lists.html',
                  {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})



# Ajout media
def ajoutmedia(request):
    formLivre = CreationLivre()
    formDVD = CreationDvd()
    formCD = CreationCd()
    formJeuDePlateau = CreationJeuDePlateau()

    if request.method == "POST":
        if  "Livre_form" in request.POST:
            formLivre = CreationLivre(request.POST)
            if formLivre.is_valid():
                livre = Livre()
                livre.name = formLivre.cleaned_data['nameLivre']
                livre.auteur = formLivre.cleaned_data['auteur']
                livre.disponible = True
                livre.save()
                livres = Livre.objects.all()
                return render(request, 'items/lists.html',
                                {'livres': livres})
            
        elif "DVD_form" in request.POST:
            formDVD = CreationDvd(request.POST)
            if formDVD.is_valid():
                dvd = Dvd()
                dvd.name = formDVD.cleaned_data['nameDVD']
                dvd.realisateur = formDVD.cleaned_data['realisateur']
                dvd.disponible = True
                dvd.save()
                dvds = Dvd.objects.all()
                return render(request, 'items/lists.html',
                                {'dvds': dvds})
            
        elif "CD_form" in request.POST:
            formCD = CreationCd(request.POST)
            if formCD.is_valid():
                cd = Cd()
                cd.name = formCD.cleaned_data['nameCD']
                cd.artiste = formCD.cleaned_data['artiste']
                cd.disponible = True
                cd.save()
                cds = Cd.objects.all()
                return render(request, 'items/lists.html',
                              {'cds': cds})
            
        elif "JeuDePlateau_form" in request.POST:
            formJeuDePlateau = CreationJeuDePlateau(request.POST)
            if formJeuDePlateau.is_valid():
                jeuDePlateau = JeuDePlateau()
                jeuDePlateau.name = formJeuDePlateau.cleaned_data['name']
                jeuDePlateau.createur = formJeuDePlateau.cleaned_data['createur']
                jeuDePlateau.save()
                jeuDePlateaux = JeuDePlateau.objects.all()
                return render(request, 'items/lists.html',
                              {'jeuDePlateaux': jeuDePlateaux})
            
    return render(request, "items/ajout_media.html", {'formLivre': formLivre, 'formDvd': formDVD, 'formCD': formCD, 'formJeuDePlateau': formJeuDePlateau})

#Emprunt

def empruntLivre(request, id):
    livre = Livre.objects.get(pk=id)
    if request.method == 'POST':
        emprunt_livre = EmpruntLivre(request.POST)
        if emprunt_livre.is_valid():
            livre.disponible = False
            livre.emprunteur = emprunt_livre.cleaned_data['emprunteur']
            livre.save()
        livres = Livre.objects.all()
        return render(request, 'items/lists.html',
                      {'livres': livres})
    else:
        empruntLivre = EmpruntLivre()
        return render(request, 'items/emprunt.html',
                      {'empruntlivre': empruntLivre})

# liste des membres
def listeemprunteur(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'emprunteurs/list.html',
                  {'emprunteurs': emprunteurs})

# Ajout membre
def ajoutmembre(request):
    formMembre = CreationMembre(request.POST)
    if request.method == "POST":
        if formMembre.is_valid():
            emprunteur = Emprunteur()
            emprunteur.name = formMembre.cleaned_data['name']
            emprunteur.NombreEmprunt = 0
            emprunteur.save()
            emprunteurs = Emprunteur.objects.all()
            return render(request, 'emprunteurs/list.html',
                          {'emprunteurs':emprunteurs})
    return render(request, "emprunteurs/ajout_emprunteur.html", {'formMembre': formMembre})

# Suppression membre
def supprimer_membre(request, id):
    emprunteur = Emprunteur.objects.get(pk=id)
    emprunteur.delete()
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'emprunteurs/list.html',
                  {'emprunteurs': emprunteurs})