from django import forms

from .models import Gallery


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['photo', 'description']
