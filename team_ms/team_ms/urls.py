from django.conf.urls import url, static
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from team_app import views
from team_app.views import TeamViewSet
from team_ms import settings

router = routers.DefaultRouter()
router.register('team', viewset=TeamViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url('get_team_list', view=views.get_team_list, name='get_team_list'),
    url('get_team_details/(?P<pk>[^/.]+)/$', view=views.get_team_details, name='get_team_details')
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
