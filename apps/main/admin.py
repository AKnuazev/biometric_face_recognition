from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'Администрирование BFR'


class BfrUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'surname', 'otchestvo', 'is_active', 'is_superuser')
    exclude = ('password', 'last_login', 'groups', 'user_permissions', 'is_superuser',
               'last_indoor', 'indoor_time', 'last_outdoor', 'outdoor_time')


admin.site.register(BfrDoor)
admin.site.register(BfrUser, BfrUserAdmin)
admin.site.unregister(Group)

