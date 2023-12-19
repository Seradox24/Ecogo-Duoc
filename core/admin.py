from django.contrib import admin

# Register your models here.

from core.models import Log

class LogAdmin(admin.ModelAdmin):
    pass



admin.site.register(Log, LogAdmin)

admin.site.site_header = 'Administración Eco-Go'
admin.site.index_title = 'Administración Eco-Go'
admin.site.site_title = 'Administración Eco-Go'