from django.contrib import admin
from . import models

#admin.site.register(models.Service)

#admin.site.register(models.ServiceFile)


from adminsortable.admin import SortableAdmin

class MySortableAdminClass(SortableAdmin):
    """Any admin options you need go here"""



#admin.site.register(models.Service, MySortableAdminClass)



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




class FileInline(admin.TabularInline):
    model = ServiceFile
    extra = 1 

class ServiceAdmin(SortableAdmin):
    inlines = [
        FileInline,
    ]


admin.site.register(Service, ServiceAdmin)





#hide groups
from django.contrib.auth.models import Group
admin.site.unregister(Group)