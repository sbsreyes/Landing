from django.db import models

# Create your models here.
class Comments(models.Model):
    email = models.CharField(max_length = 200, verbose_name = 'Email')
    value = models.IntegerField(null = True, blank=True, verbose_name='Valor Seleccionado')
    feedback = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de actualización')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    def __str__(self):
        return self.email
