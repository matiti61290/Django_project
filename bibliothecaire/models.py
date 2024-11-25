from django.db import models

class Items(models.Model):
    name = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.DateField()
    disponible = models.fields.BooleanField()
    emprunteur = models.fields.CharField(max_length=150)

class Livre(Items):
    auteur = models.fields.CharField(max_length=150)