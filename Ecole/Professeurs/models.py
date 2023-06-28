from django.db import models

# Create your models here.
"""
Professeurs
    -Photo:
    -Nom: 
    -Prenom(s):
    -Diplomes: 
    -Classes:
"""

class Prof(models.Model):
    Nom = models.CharField(max_length= 255)
    Prenoms = models.CharField(max_length= 255)
    Diplomes = models.TextField()
    Classes = models.CharField(max_length= 255,blank=True)
    Photo = models.ImageField(upload_to="Prof", blank=True, null=True)

    def __str__(self):
        return self.Nom