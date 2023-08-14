from django.contrib.auth.models import Group
from django.db.models import Model
from django.forms import ModelForm
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from common.forms import UniUserForm
from common.models import UniUser
from common.serializers import UserSerializer, GroupSerializer


# Create your views here.

# --- Standard views ---

class UniWikiUserView(CreateView):
    template_name = 'common/signup.html'
    model = UniUser
    form_class = UniUserForm


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
