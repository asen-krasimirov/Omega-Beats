from django.contrib import admin
from omega_beats.beats.models import Beat, BeatNotes, BeatPlay


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    pass


@admin.register(BeatNotes)
class BeatContentAdmin(admin.ModelAdmin):
    pass


@admin.register(BeatPlay)
class BeatPlayAdmin(admin.ModelAdmin):
    pass
