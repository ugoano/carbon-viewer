from django.urls import include, path
from django.contrib import admin

from .view_routers import router
from .buildings.views import BuildingUploadView
from .meters.views import MeterUploadView
from .readings.views import ReadingUploadView


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'buildings-upload/', BuildingUploadView.as_view()),
    path(r'meters-upload/', MeterUploadView.as_view()),
    path(r'readings-upload/', ReadingUploadView.as_view()),
    path(r'^admin/', admin.site.urls)
]
