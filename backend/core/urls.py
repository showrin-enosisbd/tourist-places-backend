from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from core.views import create_place

urlpatterns = [
    url('^places/new/', create_place, name='create-place')
]

urlpatterns = format_suffix_patterns(urlpatterns)
