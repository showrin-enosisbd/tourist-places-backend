from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from core.views import place_list, place_detail

urlpatterns = [
    url(r'^places/$', place_list, name='place-list'),
    url(r'^places/(?P<pk>\d+)/$', place_detail, name='place-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
