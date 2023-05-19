from django.core.management.base import BaseCommand
import requests
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Download place from link to .json'

    def handle(self, *args, **options):
        if not options['url']:
            return
        place_response = requests.get(options['url'])
        place_response.raise_for_status()
        place_payload = place_response.json()
        place, place_created = Place.objects.get_or_create(
            title=place_payload['title'],
            description_short=place_payload['description_short'],
            description_long=place_payload['description_long'],
            lng=place_payload['coordinates']['lng'],
            lat=place_payload['coordinates']['lat']
        )
        if not place_created:
            return
        for index, image_url in enumerate(place_payload['imgs'], 1):
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_content = ContentFile(image_response.content)
            image, image_created = Image.objects.get_or_create(
                position=index,
                place=place
            )
            if image_created:
                image.image.save(f'{place.id}_{index}',
                                 image_content, save=True)

    def add_arguments(self, parser):
        parser.add_argument('url', action='store', help='Link to .json')
