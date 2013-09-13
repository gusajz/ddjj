import json

from django.core.management.base import BaseCommand, CommandError

from ddjjapp.models import Jurisdiction


class Command(BaseCommand):
    args = '<file1 file2 ...>'
    help = 'Carga jurisdicciones de un archivo json a la base de datos'

    def _load_jurisdiction(self, jurisdiction_list):

        if jurisdiction_list is None:
            return []

        jurisdiction_models = []
        for jurisdiction in jurisdiction_list:
            current_jurisdiction_model = Jurisdiction.objects.create(
                name=jurisdiction['name'], parent=None)

            current_jurisdiction_model.save()

            if 'divisions' in jurisdiction:
                current_jurisdiction_model.jurisdiction_set = self._load_jurisdiction(
                    jurisdiction['divisions'])

            jurisdiction_models.append(current_jurisdiction_model)

        return jurisdiction_models

    def handle(self, *args, **options):
        for file_name in args:
            jurisdiction_list = json.load(open(file_name, 'r'))

            self._load_jurisdiction(jurisdiction_list)

        self.stdout.write('Successfully loaded Jurisdictions')
