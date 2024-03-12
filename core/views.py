from django.db import models
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Vessel, VesselSchedule, BillOfLanding, Container
from core.serializers import Vessel, VesselSchedule, BillOfLanding, Container

class VesselViewSet(viewsets.ViewSet):

    queryset = Vessel.objects.all()
    serializer = Vessel

class VesselScheduleViewSet(viewsets.ViewSet):

    queryset = VesselSchedule.objects.all()
    serializer = VesselSchedule

class BillOfLandingViewSet(viewsets.ViewSet):

    queryset = BillOfLanding.objects.all()
    serializer = BillOfLanding

class ContainerViewSet(viewsets.ViewSet):

    queryset = Container.objects.all()
    serializer = Container



