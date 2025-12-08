from django.contrib import admin
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "status")
    ordering = ("-timestamp",)
