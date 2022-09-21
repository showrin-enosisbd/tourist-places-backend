from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from account.views import LoginUser, register_user, logout_user, user_list, who_am_i

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^account/register/', register_user, name='register-user'),
    url('^account/login/', LoginUser.as_view(), name='login-user'),
    url('^account/logout/', logout_user, name='logout-user'),
    url('^account/users/$', user_list, name='user-list'),
    url('^account/users/me/$', who_am_i, name='who-am-i'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
