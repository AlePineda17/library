from django.contrib import admin
from .models import Organization, Activity, Subscribe

admin.site.register(Organization)
admin.site.register(Activity)

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    pass