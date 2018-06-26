from django.contrib import admin
from player_app.models import Player
from import_export.admin import ImportExportMixin


@admin.register(Player)
class PlayerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'team_id', 'high_score')
    search_fields = ('id', 'name', 'image', 'team_id', 'high_score')
