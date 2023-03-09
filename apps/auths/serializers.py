# DRF
from rest_framework import serializers

# Django
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    """Custom user serializer."""
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'last_name',
            'first_name',
            'patronymic',
            'is_active',
            'is_staff',
            'is_superuser'
        )
