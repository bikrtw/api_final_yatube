from django.contrib import admin

from posts import models

admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Follow)
admin.site.register(models.Group)
