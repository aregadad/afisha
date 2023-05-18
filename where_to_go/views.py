from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Place
from django.urls import reverse


def show_index(request):
    geo = {
        'type': 'FeatureCollection',
        'features':
        [
            {
                'type': 'Feature',
                'geometry':
                {
                    'type': 'Point',
                    'coordinates': [place.lng_coord, place.lat_coord]
                },
                'properties':
                {
                    'title': place.title,
                    'placeId': place.place_id,
                    'detailsUrl': reverse(show_place, args=[place.id])
                }
            } for place in Place.objects.all()
        ]
    }
    context = {'geo': geo}
    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    content = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates':
        {
            'lng': place.lng_coord,
            'lat': place.lat_coord
        }
    }
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
