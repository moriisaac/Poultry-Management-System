from django.urls import path, include
from rest_framework import routers
from .views import FarmViewSet, PoultryHouseViewSet, ChickenViewSet

router = routers.DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'poultry-houses', PoultryHouseViewSet)
router.register(r'chickens', ChickenViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]