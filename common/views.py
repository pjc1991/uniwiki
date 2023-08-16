from django.contrib.auth.models import Group
from django.db.models import Model
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, RedirectView
from rest_framework import viewsets

from common.forms import UniUserForm, UniUserLoginForm
from common.models import UniUser
from common.serializers import UserSerializer, GroupSerializer
from wiki import services


# Create your views here.

# --- Standard views ---

class UniWikiIndexView(RedirectView):
    # if user is logged in, redirect to wiki index
    # if user is not logged in, redirect to login page
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return '/wiki/'
        else:
            return '/login/'


class UniWikiSignupView(CreateView):
    template_name = 'common/signup.html'
    model = UniUser
    form_class = UniUserForm


class UniWikiLoginView(CreateView):
    template_name = 'common/login.html'
    model = UniUser
    form_class = UniUserLoginForm
    success_url = '/wiki/'

    def post(self, request, *args, **kwargs):
        if not services.login_user(request, *args, **kwargs):
            return redirect('/login/')
        return redirect(self.success_url)

    def form_valid(self, form):
        return redirect(self.success_url)


# --- API views ---
class CustomModelListView(ListView):
    model: Model = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = UniUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return UniUser.objects.filter(id=user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # only allow users to see their own user object

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Group.objects.all()
        else:
            return user.groups.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
