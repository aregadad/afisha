from django.shortcuts import render
from places.models import Place


def index(request):
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
                    'detailsUrl': f'static/places/{place.place_id}.json'
                }
            } for place in Place.objects.all()
        ]
    }
    context = {'geo': geo}
    return render(request, 'index.html', context)
