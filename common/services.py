
# Create your services here.

from django.contrib.auth import authenticate, login


def login_user(request, username, password):
    user = authenticate(username=username, password=password)

    if user is None:
        raise Exception("User is None")

    login(request, user)
    return True
