from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from sluds import views

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'User_OpenAuth', views.User_OpenAuthSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user/get_user_info.uds/$', views.get_user_info),
    ]
#url(r'^user/get_user_info.uds/?userid=P<0-9>+/$', views.get_user_info),
# url(r'^users/$', views.users_detail),
#urlpatterns = format_suffix_patterns(urlpatterns)