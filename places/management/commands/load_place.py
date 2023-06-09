from django.core.management.base import BaseCommand
import requests
from places.models import Place, Image
from django.core.files.base import ContentFile
from urllib.parse import urlparse
import os


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
            lng=place_payload['coordinates']['lng'],
            lat=place_payload['coordinates']['lat'],
            defaults={
                'description_short': place_payload.get('description_short', ''),
                'description_long': place_payload.get('description_long', ''),
            },
        )

        if not place_created:
            return
        for index, image_url in enumerate(place_payload['imgs'], 1):
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_extension = os.path.splitext(urlparse(image_url).path)[1]
            image_name = f'{place.id}_{index}{image_extension}'
            image_content = ContentFile(image_response.content, image_name)
            Image.objects.create(
                image=image_content,
                position=index,
                place=place,
            )

    def add_arguments(self, parser):
        parser.add_argument('url', action='store', help='Link to .json')
