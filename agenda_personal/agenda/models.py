from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Usuario",
    ) 
    
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    due_date = models.DateField(blank=True, null=True, verbose_name="Fecha Límite")
    is_completed = models.BooleanField(default=False, verbose_name="Completada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['is_completed', 'due_date', 'created_at'] 

    def __str__(self):
        return self.title