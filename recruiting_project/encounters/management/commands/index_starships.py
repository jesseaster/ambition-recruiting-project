from logging import getLogger

from django.core.management.base import BaseCommand
from manager_utils import upsert

from recruiting_project.encounters.models import StarshipClass, Starship
from recruiting_project.encounters.swapi import SWAPI


LOG = getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        swapi = SWAPI()

        for i, page in enumerate(swapi.get_starships_by_page()):
            for starship in page:
                # Create starship
                starship_class, created = upsert(
                    StarshipClass.objects,
                    name=starship['starship_class']
                )
                model_obj, created = upsert(
                    Starship.objects,
                    name=starship['name'],
                    updates={
                        'swapi_url': starship.get('url'),
                        'model': starship.get('model'),
                        'starship_class': starship_class,
                        'cost_in_credits': self._get_number_or_none(starship, 'cost_in_credits'),
                        'crew': self._get_number_or_none(starship, 'crew'),
                        'passengers': self._get_number_or_none(starship, 'passengers'),
                        'cargo_capacity': self._get_number_or_none(starship, 'cargo_capacity'),
                    }
                )
                #print(str(created) + " " + str(model_obj))
                # https://django-manager-utils.readthedocs.io/en/latest/ref/method-documentation.html?highlight=upsert#upsert
                # Have to use an identifier to upsert, otherwise you update the same one, over and over again
    def _get_number_or_none(self, obj, field_key):
        """
        Returns an integer if one can be parsed from the field, else None
        """
        try:
            return int(obj.get(field_key))
        except ValueError:
            return None

