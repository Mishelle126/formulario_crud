from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

# Create your models here.
class nombre(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=40)