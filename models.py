from asyncio.windows_events import NULL
from datetime import datetime
from distutils.command.upload import upload
from operator import truediv
from re import T
from turtle import mode
from django.db import models
from datetime import date

from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.


class Patient(models.Model):
    CIN = models.CharField(max_length=7, blank=True,
                           primary_key=True, unique=True)
    nom = models.CharField(max_length=20, blank=True)
    prenom = models.CharField(max_length=20, blank=True)
    dateNaissance = models.DateField(max_length=20, blank=True)
    genre = models.CharField(max_length=1, blank=True, choices=[
                             ('m', 'male'), ('f', 'female')])
    situationFamiliale = models.CharField(max_length=20, blank=True, choices=[(
        'marié', 'marié'), ('divorcé', 'divorcé'), ('célibataire', 'célibataire'), ('veuf', 'veuf')])
    poids = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    taille = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    IMC = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def getIMC(self):
        T = float(self.taille)*0.01
        P = float(self.poids)
        IMC = 0
        IMC = round(P/T**2, 2)
        return IMC
    type_diabete = models.IntegerField(
        choices=[(0, 0), (1, 1), (2, 2)], blank=True, null=True)
    date_decouverte_diabete = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=13, blank=True)

    def __str__(self):
        txt = "{} {}"
        return txt.format(self.nom, self.prenom)


class Oeil(models.Model):
    image_L = models.ImageField(blank=True, upload_to='Oeil_Gauche')
    stade_L = models.IntegerField(blank=True, choices=[(
        0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
    image_R = models.ImageField(blank=True, upload_to='Oeil_Droite')

    stade_R = models.IntegerField(blank=True, choices=[(
        0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def _str_(self):
        oeil = "oeil"
        return oeil


class Region(models.Model):
    region = models.CharField(max_length=20, blank=True)

    def __str__(self):
        region = "{}"
        return region.format(self.region)


class Ville(models.Model):
    ville = models.CharField(max_length=20, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        ville = "{}"
        return ville.format(self.ville)


class Etablissement_sante(models.Model):
    nom = models.CharField(max_length=40, blank=True)
    type_etablissement = models.CharField(
        max_length=20, blank=True, choices=[('CHU', 'CHU')])
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        nom = "{}"
        return nom.format(self.type_etablissement)


class Medecin(models.Model):
    nom = models.CharField(max_length=20, blank=True)
    prenom = models.CharField(max_length=20, blank=True)
    specialite = models.CharField(max_length=20, blank=True, choices=[
                                  ('Professeur', 'Professeur'), ('Resident', 'Resident')])
    etablissement_sante = models.ForeignKey(
        Etablissement_sante, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        nom = "Dr. {} {}"
        return nom.format(self.nom, self.prenom)


class Consultations(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    type_consultation = models.CharField(max_length=50, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True)
    oeil = models.ForeignKey(Oeil, on_delete=models.CASCADE, blank=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        txt = "{} {} {}/{}/{} "
        return txt.format(self.patient.nom, self.patient.prenom, self.date.year, self.date.month, self.date.day)
