

import django
from django.db.models.base import Model
from django.forms import fields, widgets
from django.conf.urls import url
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

       