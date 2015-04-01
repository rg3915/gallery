from django.db import models
from django.utils.translation import ugettext_lazy as _


class Gallery(models.Model):
    description = models.CharField(_(u'descrição'), max_length=20)
    photo = models.ImageField(upload_to='media')

    class Meta:
        ordering = ['description']
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return self.description
