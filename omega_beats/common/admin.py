from django.contrib import admin
from omega_beats.common.models import Like, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
