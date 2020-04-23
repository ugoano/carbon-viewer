
from rest_framework import routers
from .readings.views import ReadingViewSet
from .meters.views import MeterViewSet
from .buildings.views import BuildingViewSet


router = routers.DefaultRouter()
router.register(r'readings', ReadingViewSet)
router.register(r'meters', MeterViewSet)
router.register(r'buildings', BuildingViewSet)
