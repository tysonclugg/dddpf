# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import dddp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', dddp.models.AleaIdField(default=None, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('publication_state', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'public', b'Public'), (b'private', b'Private')])),
                ('authors', models.ManyToManyField(related_name='presentations', to=settings.AUTH_USER_MODEL)),
                ('invited', models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PresentationRole',
            fields=[
                ('id', dddp.models.AleaIdField(default=None, serialize=False, editable=False, primary_key=True)),
                ('can_present', models.BooleanField(default=False)),
                ('can_modify', models.BooleanField(default=False)),
                ('can_review', models.BooleanField(default=False)),
                ('can_moderate', models.BooleanField(default=False)),
                ('can_mix', models.BooleanField(default=False)),
                ('presentation', models.ForeignKey(to='slides.Presentation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', dddp.models.AleaIdField(default=None, serialize=False, editable=False, primary_key=True)),
                ('view_state', models.CharField(default=b'pending', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', dddp.models.AleaIdField(default=None, serialize=False, editable=False, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('content', models.TextField(blank=True)),
                ('content_type', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('notes_type', models.CharField(max_length=50)),
                ('publication', models.ForeignKey(to='slides.Presentation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='session',
            name='current_slide',
            field=models.ForeignKey(blank=True, to='slides.Slide', null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='present',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='session',
            name='presentation',
            field=models.ForeignKey(to='slides.Presentation'),
        ),
    ]
