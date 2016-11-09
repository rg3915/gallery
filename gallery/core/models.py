from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Gallery(TimeStampedModel):
    description = models.CharField(
        'descrição', max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='media')

    class Meta:
        ordering = ['-created']
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return self.description
