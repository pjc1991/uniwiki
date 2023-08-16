# Create your services here.
from django.contrib.auth import authenticate, login

from common.forms import UniUserLoginForm
from common.models import UniUser
from wiki.models import Universe


# check if user is available for the universe or card

def is_available_universe(user: UniUser, universe: Universe):
    # if user is None
    if user is None:
        return False

    # if user is anonymous
    if user.is_anonymous:
        return False

    # if user is superuser
    if user.is_superuser:
        return True

    # if user is owner of the universe
    if universe.owner == user:
        return True

    if universe.allowed_users.filter(id=user.id).exists():
        return True

    return False


def auth_login(request, user):
    pass


def login_user(request, *args, **kwargs) -> bool:
    form = UniUserLoginForm(request.POST)
    if not form.is_valid():
        print("Form is not valid"
              "form.errors: ", form.errors)
        raise Exception("Form is not valid")

    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)

    if user is None:
        raise Exception("User is None")

    login(request, user)
    return True
