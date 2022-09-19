from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from core.views import create_place, place_list

urlpatterns = [
    url('^places/', place_list, name='create-place'),
    url('^places/new/', create_place, name='create-place'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
