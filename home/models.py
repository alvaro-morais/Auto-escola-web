from django.db import models
from AutoEscola import settings

class Pessoa(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Agenda(models.Model):
    name = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()