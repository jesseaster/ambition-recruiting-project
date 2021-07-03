from rest_framework.viewsets import ModelViewSet

from recruiting_project.encounters.models import Starship, Encounter
from recruiting_project.encounters.serializers import StarshipSerializer, EncounterSerializer
from django_filters import rest_framework as filters


class StarshipFilter(filters.FilterSet):
    class Meta:
        model = Starship
        fields = ('name', 'starship_class__name')


class StarshipsModelViewSet(ModelViewSet):
    """
    Model viewset for starships API
    """
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    filterset_class = StarshipFilter


class EncountersModelViewSet(ModelViewSet):
    """
    Model viewset for encounters API
    """
    queryset = Encounter.objects.prefetch_related('mobs__starship')
    serializer_class = EncounterSerializer
