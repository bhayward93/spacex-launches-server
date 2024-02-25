from rest_framework.response import Response
from rest_framework.decorators import api_view
from dataclasses import dataclass
import requests;

# View that gets past launch data from SpaceX data API.
@api_view(['GET'])
def getPast(request):
    try:
        response = requests.get('https://api.spacexdata.com/v5/launches/past')
        responseJson = response.json()

        if len(responseJson) is 0:
            raise Exception('No results found')

        arr = []

        for launch in responseJson:
            arr.append(
                {
                    'name': launch['name'],
                    'success': launch['success'],
                    'flight_number': launch['flight_number'],
                    'failures': launch['failures'],
                    'timestamp': launch['date_unix'],
                    'links': {
                        'webcast_url': launch['links']['webcast'],
                        'article_url': launch['links']['article'],
                        'wikipedia_url': launch['links']['wikipedia']
                    }
                }
            );

        return Response(
            status = 200,
            data = arr
        )
    except Exception as e:
        print(e)
        return Response(
            status = 500
        )