from django.contrib import admin
from truecaller import models
# Register your models here.

admin.site.register(models.UserContacts)
admin.site.register(models.UserProfile)
admin.site.register(models.Spam)