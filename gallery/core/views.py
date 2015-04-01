from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Gallery


def home(request):
    return render(request, 'index.html')


class GalleryList(ListView):
    template_name = 'gallery_list.html'
    model = Gallery
    context_object_name = 'gallery'


class GalleryCreate(CreateView):
    template_name = 'gallery_create_form.html'
    model = Gallery
    success_url = reverse_lazy('gallery_list')
