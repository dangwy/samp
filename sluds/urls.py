from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
#from sluds import views

from .views import get_user_info, update_user_info
from .views import localregist_user_email, checkin_email

router = routers.DefaultRouter()
#router.register(r'Users', views.UserViewSet)
#router.register(r'User_OpenAuth', views.User_OpenAuthSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^user/get_token_auth.luds', views.obtain_auth_token), # 获取token
    url(r'^user/get_user_info.luds', get_user_info),
    url(r'^user/update_user_info.luds', update_user_info),
    url(r'^user/localregist_user_email.luds', localregist_user_email),
    url(r'^user/checkin_email.luds', checkin_email),
    ]
#url(r'^user/get_user_info.uds/?userid=P<0-9>+/$', views.get_user_info),
#url(r'^users/$', views.users_detail),
#urlpatterns = format_suffix_patterns(urlpatterns)