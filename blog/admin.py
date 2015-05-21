from django.contrib import admin
from . import models

admin.site.register(models.Usluga)

#nie potrzebne nam bo sie wyswietla w wnetrzu uslugi
#admin.site.register(models.Employee)



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from blog.models import Pozwolenie
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Pokazpozwolenie(admin.StackedInline):
    model = Pozwolenie
    can_delete = False
    verbose_name_plural = 'Uprawnienia'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (Pokazpozwolenie, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)