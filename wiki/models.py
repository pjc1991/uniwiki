from django.db import models

from common.models import BaseModel


# Create your models here.


class Universe(BaseModel):
    """
    A universe is a collection of Objects, which can be edited by allowed users.
    """

    # id as primary key
    id = models.AutoField(primary_key=True)

    # name of the universe
    name = models.CharField(max_length=255, help_text="Name of the universe")

    # description of the universe
    description = models.TextField(help_text="Description of the universe")

    # created time
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created time")

    # modified time
    modified_at = models.DateTimeField(auto_now=True, help_text="Modified time")

    # owner of the universe
    owner = models.ForeignKey('common.UniUser', related_name='owned_universes', on_delete=models.CASCADE,
                              help_text="Owner of the universe")

    # allowed users
    allowed_users = models.ManyToManyField('common.UniUser', related_name='allowed_universes', blank=False,
                                           help_text="Allowed users")

    def __str__(self):
        return self.name


class WikiDocument(BaseModel):
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
        UNKNOWN = 'UNKNOWN', 'Unknown'

    # id as primary key
    id = models.AutoField(primary_key=True, help_text="Primary key")

    # name of the document
    name = models.CharField(max_length=255, help_text="Name of the document")

    # description of the document
    description = models.TextField(help_text="Description of the document")

    # content of the document
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, blank=False, help_text="Universe of the document")

    # owner of the document
    owner = models.ForeignKey('common.UniUser', related_name='owned_objects', on_delete=models.CASCADE, blank=False,
                              help_text="Owner of the document")

    # allowed users
    version = models.IntegerField(default=0, null=False, help_text="Version of the document")

    # related documents
    related_documents = models.ManyToManyField('self', blank=True, help_text="Related documents")

    # type of the document
    document_type = models.CharField(max_length=255, choices=DocumentType.choices, null=False,
                                     help_text="Type of the document")

    # created time
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created time")

    # modified time
    modified_at = models.DateTimeField(auto_now=True, help_text="Modified time")

    # is published
    is_published = models.BooleanField(default=False, help_text="Is published")

    # is deleted
    is_deleted = models.BooleanField(default=False, help_text="Is deleted")

    def __str__(self):
        return self.name
