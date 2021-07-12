from django.contrib import admin
from omega_beats.api.models import Beat


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    pass
