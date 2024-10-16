"""
URL configuration for audio_analyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from audio_analyzer_app.views import PromptViewSet, PromptAssociationViewSet, AudioViewSet


audio_analyzer_router = routers.DefaultRouter()
audio_analyzer_router.register('prompts', PromptViewSet)
audio_analyzer_router.register('prompt-associations', PromptAssociationViewSet)
audio_analyzer_router.register('audios', AudioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(audio_analyzer_router.urls)),
    path('', include('authorization.urls'))
]
