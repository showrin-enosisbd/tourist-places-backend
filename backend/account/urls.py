from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from django.contrib import admin

from account.views import register_user, logout_user, user_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^account/register/', register_user, name='register-user'),
    url('^account/login/', views.obtain_auth_token),
    url('^account/logout/', logout_user, name='logout-user'),
    url('^account/users/', user_list, name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
