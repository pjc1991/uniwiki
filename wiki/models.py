from django.db import models


# Create your models here.


class Universe(models.Model):
    """
    A universe is a collection of Objects, which can be edited by allowed users.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='owned_universes', on_delete=models.CASCADE)
    allowed_users = models.ManyToManyField('auth.User', related_name='allowed_universes', blank=False)

    def __str__(self):
        return self.name


class WikiDocument(models.Model):
    """
    A WikiDocument is a thing that can be edited by users,
    including characters, plot, setting, etc.
    """

    class DocumentType(models.TextChoices):
        """
        The type of the Wiki document.
        """
        CHARACTER = 'CHARACTER', 'Character'
        PLOT = 'PLOT', 'Plot'
        SETTING = 'SETTING', 'Setting'
        ITEM = 'ITEM', 'Item'
        OTHER = 'OTHER', 'Other'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, blank=False)
    owner = models.ForeignKey('auth.User', related_name='owned_objects', on_delete=models.CASCADE, blank=False)
    version = models.IntegerField(default=0)

    related_documents = models.ManyToManyField('self', blank=True)
    document_type = models.CharField(max_length=255, choices=DocumentType.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
