from django.db import models

class Items(models.Model):
    name = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.DateField()
    disponible = models.fields.BooleanField()
    emprunteur = models.fields.CharField(max_length=150)

class Livre(Items):
    auteur = models.fields.CharField(max_length=150)

class Dvd(Items):
    realisateur = models.fields.CharField(max_length=150)

class Cd(Items):
    artiste = models.fields.CharField(max_length=150)

class JeuDePlateau(models.Model):
    name = models.fields.CharField(max_length=150)

class Emprunteur(models.Model):
    name = models.fields.CharField(max_length=150)
    NombreEmprunt = models.fields.FloatField()