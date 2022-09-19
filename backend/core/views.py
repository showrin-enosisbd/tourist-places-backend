from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.serializers import PlaceSerializer


@api_view(['POST'])
def create_place(request, format=None):
    try:
        serializer = PlaceSerializer(data=request.data)

        if serializer.is_valid():
            new_place = serializer.save()

            response = {
                'message': 'The place has been created successfully',
                'id': new_place.id,
            }

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response(err.__str__(), status=status.HTTP_400_BAD_REQUEST)
