from django.contrib import admin
from .models import Link

# Register your models here.
class MyAppModelAdmin(admin.ModelAdmin):
    list_display = ["url", "short_url", "last_updated"]

    class Meta:
        model = Link

admin.site.register(Link, MyAppModelAdmin)
admin.site.site_header = 'My Admin'

