
from django.urls import path, include

from rest_framework import routers

from rest_framework.authtoken import views as authtoken_views

from .views import register, login_view, logout_view, TokenViewSetNative


authorization_router = routers.DefaultRouter()
authorization_router.register('tokens', TokenViewSetNative)

urlpatterns = [
    path('register/', register, name='registration'),
    path('login/', login_view, name='authorization'),
    path('logout/', logout_view, name='logout'),
    path('get_token/', authtoken_views.obtain_auth_token, name='get_token'),
    path('', include(authorization_router.urls))
]