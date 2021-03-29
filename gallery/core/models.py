from mimetypes import guess_type

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
        'descrição',
        max_length=20,
        null=True,
        blank=True
    )
    photo = models.ImageField('foto', upload_to='', null=True, blank=True)
    file = models.FileField('arquivo', upload_to='', null=True, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        if self.description:
            return self.description
        return str(self.pk)

    @property
    def get_filename(self):
        if self.photo or self.file:
            return self.photo.name or self.file.name

    @property
    def get_type(self):
        if self.photo:
            _mimetypes, _ = guess_type(self.photo.name)
            return _mimetypes
        if self.file:
            _mimetypes, _ = guess_type(self.file.name)
            return _mimetypes
