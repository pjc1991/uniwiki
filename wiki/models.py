from django.db import models

# Create your models here.


class Universe(models.Model):
    """
    A universe is a collection of Objects, which can be edited by allowed users.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='owned_universes', on_delete=models.CASCADE)
    allowed_users = models.ManyToManyField('auth.User', related_name='allowed_universes')

    def __str__(self):
        return self.name

