from django.urls import path

from gallery.core import views as c

app_name = 'core'

urlpatterns = [
    path('', c.home, name='home'),
    path('gallery/', c.GalleryList.as_view(), name='gallery_list'),
    path('add/', c.GalleryCreate.as_view(), name='gallery_add'),

]
