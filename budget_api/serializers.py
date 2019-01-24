"""Define serializers for use with budget auth API."""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Create a serializer for user passwords."""
    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
            )

    def create(self, validated_data):
        """Ensure data passed in is valid before saving the user."""
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user
