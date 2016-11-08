from django.conf.urls import url
from gallery.core import views as c


urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^gallery/$', c.GalleryList.as_view(), name='gallery_list'),
    url(r'^add/$', c.GalleryCreate.as_view(), name='gallery_add'),

]
