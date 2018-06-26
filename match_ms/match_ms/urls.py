from django.conf.urls import url, static
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from match_app import views
from match_app.views import MatchViewSet
from match_ms import settings

router = routers.DefaultRouter()
router.register('match', viewset=MatchViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url('get_all_match', views.get_all_match, name='get_all_match')
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
