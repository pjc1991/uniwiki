from django.contrib import admin

from wiki.models import Universe, WikiDocument

# Register your models here.

admin.site.register(Universe)
admin.site.register(WikiDocument)