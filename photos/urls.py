from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    re_path('',views.home,name ='images'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^image/',views.image,name='image')
]
if settings.DEBUG is True:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)