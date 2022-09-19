from rest_framework import serializers

from core.models import Place


class PlaceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    name = serializers.CharField()
    address = serializers.CharField()
    rating = serializers.IntegerField()
    type = serializers.CharField()
    picture = serializers.CharField()

    def create(self, validated_data):
        new_place = Place.objects.create(**validated_data)

        return new_place
