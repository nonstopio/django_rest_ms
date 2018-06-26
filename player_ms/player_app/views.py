import json
from urllib import request, parse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from player_app.models import Player
from player_app.serializer import PlayerSerializer

from player_app.services.common import MSUrls


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


@api_view(['GET', 'POST'])
def get_players(req):
    players = PlayerSerializer(
        Player.objects.all(),
        many=True
    ).data

    team_id_list = []

    for one_player in players:
        team_id_list.append(one_player['team_id'])

    data = parse.urlencode({'team_ids': team_id_list}).encode('utf-8')

    team_data_list = json.loads(
        request.urlopen(MSUrls.team + 'get_player_team/', data=data).read()
    )

    count = 0
    for one_player in players:
        one_player['team'] = team_data_list[count]
        count = count + 1

    return Response(players)


@api_view(['GET'])
def fake_100_players(req):

    count = 1
    while count < 201:
        Player.objects.create(
            name='Name ' + str(count),
            image='',
            team_id=2,
            high_score=123
        ).save()
        count = count + 1

    return Response('Done!')


@api_view(['GET'])
def get_team_players(req, pk):
    players_list = PlayerSerializer(
        Player.objects.filter(team_id=pk),
        many=True
    ).data

    return Response(players_list)
