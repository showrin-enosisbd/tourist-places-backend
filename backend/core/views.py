from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from core.serializers import PlaceSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_place(request, format=None):
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
