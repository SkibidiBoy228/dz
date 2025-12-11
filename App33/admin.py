from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "status", "user_link")
    ordering = ("-timestamp",)

    def user_link(self, obj):
        u = obj.user
        url = reverse("admin:auth_user_change", args=[u.id])
        return format_html(
            '<a href="{}">{}(id={}) {}</a>',
            url,
            u.first_name,
            u.id,
            u.last_name
        )
    user_link.short_description = "Користувач"
