from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.alumno.nombreAlumno} - {self.curso.nombreCurso}: {self.nota}"