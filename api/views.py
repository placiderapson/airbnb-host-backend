from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST)

from .models import LocationInfo
from .serializers import LocationInfoSerializer

# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls = {
        'Post Location Info [POST]': '/api/v1/post-location-info',
        'Get Location Info [GET]': '/api/v1/get-location-info',
    }

    return Response(
        {'message': 'Welcome to the Airbnb Host Sample API',
         'endpoints': api_urls}, HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def post_location_info(request):
    serializer = LocationInfoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        message = {'warning': 'Something is wrong with your Data'}

        return Response(message, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_location_info(request):
    info = LocationInfo.objects.all()

    if not info:
        message = {'warning': 'Something is wrong with your Data'}

        return Response(message, HTTP_400_BAD_REQUEST)

    else:
        serializer = LocationInfoSerializer(info, many=True)

        return Response(serializer.data, HTTP_200_OK)
