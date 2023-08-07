from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Base model for all models
    """
    # Primary key, auto increment
    id = models.AutoField(primary_key=True, db_index=True, help_text="Primary key")

    # Created time
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created time")

    # Updated time
    updated_at = models.DateTimeField(auto_now=True, help_text="Updated time")

    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self):
        """
        admin page will show the object's id
        if there is no __str__ method override
        """
        return str(self.id)


class UniUser(AbstractUser):
    """
    Custom user model
    """

    # There is nothing to customize for now
    # However, we can add more fields here when needed

    objects = UserManager()

    def __str__(self):
        return self.username
