from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.partners.models import Gym, Caterer
from apps.partners.serializers import GymSerializer, CatererSerializer, CatererDetailSerializer


class GymListAPIView(generics.ListAPIView):
    """List of gyms"""
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = (IsAuthenticated,)


class CatererListAPIView(generics.ListAPIView):
    """List of caterers"""
    queryset = Caterer.objects.all()
    serializer_class = CatererSerializer
    permission_classes = (IsAuthenticated,)


class CatererDetailAPIView(generics.RetrieveAPIView):
    """Get a particular caterer via its id"""
    queryset = Caterer.objects.all()
    serializer_class = CatererDetailSerializer
    permission_classes = (IsAuthenticated,)
