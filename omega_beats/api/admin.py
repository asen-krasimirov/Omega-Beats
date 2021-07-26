from django.contrib import admin
from omega_beats.api.models import Beat, BeatNotes


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    pass


@admin.register(BeatNotes)
class BeatContentAdmin(admin.ModelAdmin):
    pass
