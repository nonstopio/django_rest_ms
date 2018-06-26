from rest_framework import viewsets

from match_app.models import Match
from match_app.serializer import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
