from django.contrib.auth.forms import UserCreationForm

from common.models import UniUser


# create your forms here.

class UniUserForm(UserCreationForm):
    class Meta:
        model = UniUser
        fields = ('username', 'email', 'password1', 'password2')


class UniUserLoginForm(UserCreationForm):
    class Meta:
        model = UniUser
        fields = ('username', 'password1')
