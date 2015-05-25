from django.contrib import admin
from . import models

admin.site.register(models.Service)

#nie potrzebne nam bo sie wyswietla w wnetrzu uslugi
#admin.site.register(models.Employee)



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from servicelist.models import *
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PermissionAdmin(admin.StackedInline):
    model = Permission
    can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PermissionAdmin, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)