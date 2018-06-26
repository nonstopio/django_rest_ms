from django.conf.urls import url, static
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from player_app import views
from player_app.views import PlayerViewSet
from player_ms import settings

router = routers.DefaultRouter()
router.register('player', viewset=PlayerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url('get_players', view=views.get_players, name='get_players'),
    url('fake_100_players', view=views.fake_100_players, name='fake_100_players'),
    url(r'^get_team_players/(?P<pk>[^/.]+)/$', view=views.get_team_players, name='get_team_players'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
