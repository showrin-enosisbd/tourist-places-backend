from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"), allow_null=False)
    email = serializers.EmailField(label=_("Email"), allow_null=False)
    password = serializers.CharField(label=_("Password"),
                                     style={'input_type': 'password'},
                                     trim_whitespace=False)
    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        account = User.objects.create(**validated_data)
        password = self.validated_data["password"]
        account.set_password(password)
        return account
