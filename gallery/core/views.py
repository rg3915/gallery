from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy as r
from .models import Gallery
from .forms import GalleryForm


def home(request):
    return render(request, 'index.html')


class GalleryList(ListView):
    template_name = 'core/gallery_list.html'
    model = Gallery
    context_object_name = 'gallery'


class GalleryCreate(CreateView):
    template_name = 'core/gallery_form.html'
    model = Gallery
    form_class = GalleryForm
    success_url = r('core:gallery_list')
