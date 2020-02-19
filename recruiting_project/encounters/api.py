from rest_framework.viewsets import ModelViewSet

from recruiting_project.encounters.models import Starship, Encounter
from recruiting_project.encounters.serializers import StarshipSerializer, EncounterSerializer


class StarshipsModelViewSet(ModelViewSet):
    """
    Model viewset for starships API
    """
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class EncountersModelViewSet(ModelViewSet):
    """
    Model viewset for encounters API
    """
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
