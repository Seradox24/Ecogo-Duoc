from django.contrib import admin

# Register your models here.

from core.models import Log

class LogAdmin(admin.ModelAdmin):
    pass



admin.site.register(Log, LogAdmin)