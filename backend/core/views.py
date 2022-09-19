from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Place
from core.serializers import PlaceSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def place_list(request, format=None):
    if request.method == 'GET':
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            serializer = PlaceSerializer(data=request.data)

            if serializer.is_valid():
                new_place = serializer.save()

                response = {
                    'message': 'The place has been created successfully',
                    'place': {
                        'id': new_place.id,
                        'name': new_place.name,
                        'address': new_place.address,
                        'rating': new_place.rating,
                        'type': new_place.type,
                        'picture': new_place.picture,
                    }
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err.__str__(), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def place_detail(request, pk, format=None):
    print(pk)
    try:
        place = Place.objects.get(pk=pk)
    except Exception as err:
        return Response(err.__str__(), status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PlaceSerializer(place, data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message': 'The place has been updated successfully',
            }

            return Response(response, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        place.delete()

        response = {
            'message': 'The place has been deleted successfully',
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)
