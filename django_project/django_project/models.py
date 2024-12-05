from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta, timezone
from django.utils import timezone
from django.db.models import (OuterRef, Subquery)


def restrict_amount(value):
        if Media.objects.filter(emprunter_id=value).count() > 2:
            raise ValidationError('max atteint pour ce membre (3)')     
        if Media.objects.filter(emprunter_id=value, bloque=1):
            raise ValidationError('il y a un retard pour ce membre')

class Emprunter(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.fields.CharField(max_length=25)
        bloque = models.fields.BooleanField(blank=True, null=True)
        def __str__(self):
            return f'{self.name}' 
          

class Media(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.fields.CharField(max_length=25)
    disponible = models.fields.BooleanField()
    dateEmprunt = models.fields.DateTimeField(default=None, null=True)
    dateBack = models.fields.DateTimeField(default=None, null=True)
    bloque = models.fields.BooleanField(blank=True, null=True, default=False)
    emprunter = models.ForeignKey(Emprunter ,related_name="emprunter", on_delete=models.DO_NOTHING, null=True, blank=True ,validators=(restrict_amount, ))    
    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.emprunter_id != None:
            self.dateEmprunt = now
            self.dateBack = self.dateEmprunt + timedelta(weeks=1)
        elif self.emprunter_id == None:
            self.dateEmprunt = None
            self.dateBack = None
        super().save(*args, **kwargs)   

class Livre(Media):
    auteur = models.fields.CharField(max_length=25)
    def save(self, *args, **kwargs):
        if self.emprunter_id != None:
           self.disponible = False
        elif self.emprunter_id == None:
             self.disponible = True
        super().save(*args, **kwargs)


class Cd(Media):
    artiste = models.fields.CharField(max_length=25)
    def save(self, *args, **kwargs):
        if self.emprunter_id != None:
           self.disponible = False
        elif self.emprunter_id == None:
             self.disponible = True
        super().save(*args, **kwargs)

class Dvd(Media):
    realisateur = models.fields.CharField(max_length=25)
    def save(self, *args, **kwargs):
        if self.emprunter_id != None:
           self.disponible = False
        elif self.emprunter_id == None:
             self.disponible = True
        super().save(*args, **kwargs)


class JeuDePlateau(models.Model):
    name = models.fields.CharField(max_length=25)
    createur = models.fields.CharField(max_length=25)
    def __str__(self):
        return f'{self.name}'


