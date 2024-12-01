from django.shortcuts import render, redirect
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur
from bibliothecaire.forms import CreationLivre, CreationCd, CreationDvd, CreationJeuDePlateau, CreationMembre, EmpruntLivre, EmpruntDvd, EmpruntCd
from django.utils import timezone

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
    # Emprunt Livre
def empruntLivre(request, livre_id):
    if request.method == 'POST':
        livre = Livre.objects.get(id=livre_id)
        emprunteur = Emprunteur.objects.get(id=request.POST['emprunteur'])
        emprunt_livre = EmpruntLivre(request.POST)
        if emprunt_livre.is_valid():
            livre.disponible = False
            livre.emprunteur = emprunteur
            livre.dateEmprunt = timezone.now()
            livre.save()
        livres = Livre.objects.all()
        return render(request, 'items/lists.html',
                      {'livres': livres})
    else:
        empruntLivre = EmpruntLivre()
        return render(request, 'items/emprunt/emprunt_livre.html',
                      {'empruntlivre': empruntLivre})

def retourLivre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if livre.emprunteur:
        livre.disponible = True
        livre.emprunteur = None
        livre.save()
    livres = Livre.objects.all()
    return render(request, 'items/lists.html',
                  {'livres': livres})

    # Emprunt Dvd
def empruntDvd(request, dvd_id):
    if request.method == 'POST':
        dvd = Dvd.objects.get(id=dvd_id)
        emprunteur = Emprunteur.objects.get(id=request.POST['emprunteur'])
        emprunt_dvd = EmpruntDvd(request.POST)
        if emprunt_dvd.is_valid():
            dvd.disponible = False
            dvd.emprunteur = emprunteur
            dvd.dateEmprunt = timezone.now()
            dvd.save()
        dvds = Dvd.objects.all()
        return render(request, 'items/lists.html',
                      {'dvds': dvds})
    else:
        empruntDvd = EmpruntDvd()
        return render(request, 'items/emprunt/emprunt_dvd.html',
                      {'empruntdvd': empruntDvd})

def retourDvd(request, dvd_id):
    dvd = Dvd.objects.get(id=dvd_id)
    if dvd.emprunteur:
        dvd.disponible = True
        dvd.emprunteur = None
        dvd.save()
    dvds = Dvd.objects.all()
    return render(request, 'items/lists.html',
                  {'dvds': dvds})

    # emprunt CD
def empruntCd(request, cd_id):
    if request.method == 'POST':
        cd = Cd.objects.get(id=cd_id)
        emprunteur = Emprunteur.objects.get(id=request.POST['emprunteur'])
        emprunt_cd = EmpruntCd(request.POST)
        if emprunt_cd.is_valid():
            cd.disponible = False
            cd.emprunteur = emprunteur
            cd.dateEmprunt = timezone.now()
            cd.save()
        cds = Cd.objects.all()
        return render(request, 'items/lists.html',
                      {'cds': cds})
    else:
        empruntCd = EmpruntCd()
        return render(request, 'items/emprunt/emprunt_cd.html',
                      {'empruntcd': empruntCd})

def retourCd(request, cd_id):
    cd = Cd.objects.get(id=cd_id)
    if cd.emprunteur:
        cd.disponible = True
        cd.emprunteur = None
        cd.save()
    cds = Cd.objects.all()
    return render(request, 'items/lists.html',
                  {'cds': cds})
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