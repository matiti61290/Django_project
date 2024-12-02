from django.db import models

class Emprunteur(models.Model):
    name = models.fields.CharField(max_length=150)
    NombreEmprunt = models.fields.IntegerField()

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.DateTimeField(null=True, blank=True)
    disponible = models.fields.BooleanField(blank=True, null=True)
    emprunteur = models.ForeignKey(Emprunteur, null=True, blank=True, on_delete=models.SET_NULL)

class Livre(Items):
    auteur = models.fields.CharField(max_length=150)

class Dvd(Items):
    realisateur = models.fields.CharField(max_length=150)

class Cd(Items):
    artiste = models.fields.CharField(max_length=150)

class JeuDePlateau(models.Model):
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)

