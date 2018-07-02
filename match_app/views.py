import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import parse as url_parse, request as url_req

from match_app.models import Match
from match_app.serializer import MatchSerializer
from match_app.services.common import MSUrls


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


@api_view(['GET'])
def get_all_match(req):
    all_match = MatchSerializer(
        Match.objects.all(),
        many=True
    ).data

    team_id_list = []

    for one_match in all_match:
        team_id_list.append({
            "team_a": one_match['team_a_id'],
            "team_b": one_match['team_b_id']
        })

    data = url_parse.urlencode({"team_ids": json.dumps(team_id_list)}).encode('utf-8')

    team_data_list = json.loads(
        url_req.urlopen(MSUrls.team + 'get_match_team/', data=data).read()
    )

    count = 0
    for one_match in all_match:
        one_match['team_a'] = team_data_list[count]['team_a']
        one_match['team_b'] = team_data_list[count]['team_b']
        count = count + 1

    return Response(all_match)
