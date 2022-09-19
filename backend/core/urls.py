from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from core.views import place_list

urlpatterns = [
    url('^places/', place_list, name='place-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
