from django import forms
from django.core.exceptions import ValidationError

from .models import Gallery


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('photo', 'file', 'description')

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('photo') and not self.cleaned_data.get('file'):
            raise ValidationError('Insira uma foto ou um arquivo.')

        return self.cleaned_data
