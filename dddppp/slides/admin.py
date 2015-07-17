from __future__ import absolute_import
from django.contrib import admin
from . import models

admin.site.register(models.Presentation)
admin.site.register(models.PresentationRole)
admin.site.register(models.Session)
admin.site.register(models.Slide)
