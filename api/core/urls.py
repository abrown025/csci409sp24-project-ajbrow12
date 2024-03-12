from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import VesselViewSet, VesselScheduleViewSet, BillOfLandingViewSet, ContainerViewSet

router = DefaultRouter()
router.register(r'vessel', VesselViewSet)
router.register(r'vessel schedule', VesselScheduleViewSet)
router.register(r'bill of landing', BillOfLandingViewSet)
router.register(r'container', ContainerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]