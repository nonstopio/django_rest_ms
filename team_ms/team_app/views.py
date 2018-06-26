import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from team_app.models import Team
from team_app.serializer import TeamSerializer
from urllib import request as http_req

from team_app.services.common import MSUrls


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


@api_view(['GET', 'POST'])
def get_team_list(req):
    team_id_list = json.loads(req.data['team_ids'])

    team_list = []
    for one_id in team_id_list:
        team_list.append(
            TeamSerializer(Team.objects.get(id=one_id), many=False).data
        )

    return Response(team_list)


@api_view(['GET'])
def get_team_details(req, pk):
    try:
        current_team = TeamSerializer(
            Team.objects.get(id=pk),
            many=False
        ).data
    except Team.DoesNotExist:
        current_team = 'No Content'
        return Response({
            'team_details': current_team,
        }, status=204)

    players = json.loads(
        http_req.urlopen(MSUrls.player + 'get_team_players/' + str(current_team['id']) + '/').read()
    )

    current_team['players'] = players

    return Response({
        'team_details': current_team,
    })
