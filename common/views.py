from django.contrib.auth.models import Group
from django.db.models import Model
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, RedirectView
from rest_framework import viewsets

from common import services
from common.forms import UniUserForm
from common.models import UniUser
from common.serializers import UserSerializer, GroupSerializer


# Create your views here.


# --- API views ---