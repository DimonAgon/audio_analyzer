from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, logout

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .permissions import general_permission_classes
from .serializers import TokenSerializerNative, UserSerializer

from authorization.forms import NativeUserCreationForm, NativeAuthenticationForm
from authorization.infrastructure.enums import *


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = NativeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = NativeUserCreationForm()

    context = {
        'form': form,
        'authorization_type': Authorization_type.REGISTRATION
    }
    return render(request, 'registration_window.html', context=context)

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NativeAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = NativeAuthenticationForm()

    context = {
        'form': form,
        'authorization_type': Authorization_type.LOGGING_IN
    }
    return render(request, 'log_in_window.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('authorization')


class TokenViewSetNative(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializerNative
    permission_classes = general_permission_classes

    def list(self, request):
        user = request.user
        queryset = Token.objects.filter(user=user)
        serializer = TokenSerializerNative(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = general_permission_classes
    http_method_names = ['get', 'put', 'update']

    def list(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)