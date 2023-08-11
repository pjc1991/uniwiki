# Create your services here.
from wiki.models import Universe
from common.models import UniUser


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


    return  False