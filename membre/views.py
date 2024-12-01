from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau

def listemedia(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeuxdeplateau = JeuDePlateau.objects.all()
    return render(request, 'listes.html',
                  {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeuxdeplateau': jeuxdeplateau})