# Generated by Django 4.2.2 on 2023-06-26 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('allowed_users', models.ManyToManyField(related_name='allowed_universes', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_universes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WikiDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('version', models.IntegerField(default=0)),
                ('document_type', models.CharField(choices=[('CHARACTER', 'Character'), ('PLOT', 'Plot'), ('SETTING', 'Setting'), ('ITEM', 'Item'), ('OTHER', 'Other')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_objects', to=settings.AUTH_USER_MODEL)),
                ('related_documents', models.ManyToManyField(related_name='related_documents', to='wiki.wikidocument')),
                ('universe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.universe')),
            ],
        ),
    ]