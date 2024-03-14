from django.db import models

#ORM 

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=75)
    fechaNacimiento=models.CharField(max_length=50)
    #creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.apellido, self.email, self.fechaNacimiento)