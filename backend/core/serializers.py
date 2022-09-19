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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.type = validated_data.get('type', instance.type)
        instance.picture = validated_data.get('picture', instance.picture)

        instance.save()

        return instance
