import requests
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy as r
from django.views.generic import CreateView, DetailView, ListView

from .forms import GalleryForm
from .models import Gallery


def home(request):
    return render(request, 'index.html')


class GalleryList(ListView):
    template_name = 'core/gallery_list.html'
    model = Gallery
    context_object_name = 'gallery'


class GalleryDetail(DetailView):
    template_name = 'core/gallery_detail.html'
    model = Gallery


class GalleryCreate(CreateView):
    template_name = 'core/gallery_form.html'
    model = Gallery
    form_class = GalleryForm
    success_url = r('core:gallery_list')


def download(request, pk):
    obj = Gallery.objects.get(pk=pk)

    file_data = None
    if obj.photo:
        # file_data = obj.photo.path
        file_data = obj.photo.url
    if obj.file:
        # file_data = obj.file.path
        file_data = obj.file.url

    if file_data:
        resp = requests.get(file_data)
        filename = file_data.split('/')[-1]
        response = HttpResponse(resp.content, content_type='image/jpeg')
        # Sem extensão do arquivo.
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
    return Http404
