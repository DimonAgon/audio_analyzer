
from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NativeUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={'class': "field", 'autofocus': True}
        )
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={'type': "email", 'class': "field"}
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.TextInput(
            attrs={'type': "password", 'class': "field"}
        )
    )

    password2 = forms.CharField(
        label="Password re-enter",
        widget=forms.TextInput(
            attrs={'type': "password", 'class': "field"}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NativeAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={'class': "field", 'autofocus': True}
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.TextInput(
            attrs={'type': "password", 'class': "field"}
        )
    )