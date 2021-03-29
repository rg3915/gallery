from django.http import FileResponse, Http404
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

    file_path = None
    if obj.photo:
        file_path = obj.photo.path
    if obj.file:
        file_path = obj.file.path

    if file_path:
        # Retorna somente o nome do arquivo.
        filename = file_path.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    return Http404
