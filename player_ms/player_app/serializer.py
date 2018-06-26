from rest_framework import serializers

from player_app.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'image', 'team_id', 'high_score')
