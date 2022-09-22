from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from core.models import Place
from core.serializers import PlaceSerializer
from core.permissions import has_permission_for_item
from helpers.pagination import get_paginted_result
from core.sorting import get_sorted_data
from core.filters import search_text_filter

PAGE_SIZE = 10


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def place_list(request, format=None):
    if request.method == 'GET':
        places = Place.objects.all()
        places = get_sorted_data(queryset=places, request=request)
        places = search_text_filter(queryset=places, request=request)

        return get_paginted_result(queryset=places, request=request,
                                   page_size=PAGE_SIZE, serializer=PlaceSerializer)

    elif request.method == 'POST':
        try:
            serializer = PlaceSerializer(data=request.data)

            if serializer.is_valid():
                new_place = serializer.save()
                new_place.creator = request.user
                new_place.save()

                response = {
                    'message': 'The place has been created successfully',
                    'place': {
                        'id': new_place.id,
                        'name': new_place.name,
                        'address': new_place.address,
                        'rating': new_place.rating,
                        'type': new_place.type,
                        'picture': new_place.picture,
                        'creator': new_place.creator.id,
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
    place = get_object_or_404(Place, pk=pk)

    if not has_permission_for_item(request, place):
        raise PermissionDenied

    else:
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
