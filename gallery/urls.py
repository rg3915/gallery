from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from gallery.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'gallery.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^gallery/$', GalleryList.as_view(), name='gallery_list'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT)
#     urlpatterns += patterns(
#         '',
#         url(r'^admin/', include(admin.site.urls)),
#     )
