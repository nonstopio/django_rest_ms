from rest_framework import serializers

from match_app.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'team_a_id', 'team_b_id', 'venue', 'start_time')
