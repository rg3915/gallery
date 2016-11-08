from django.db import models


class Gallery(models.Model):
    description = models.CharField(
        'descrição', max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='media')

    class Meta:
        ordering = ['description']
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return self.description
