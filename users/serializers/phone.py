from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from users.exceptions.not_registered import AccountNotRegisteredException
from users.models import PhoneNumber

User = get_user_model()

class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize phone number.
    """
    phone_number = PhoneNumberField()

    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)

    def validate_phone_number(self, value):
        try:
            queryset = User.objects.get(phone__phone_number=value)
            if queryset.phone.is_verified == True:
                err_message = _('Phone number is already verified')
                raise serializers.ValidationError(err_message)

        except User.DoesNotExist:
            raise AccountNotRegisteredException()

        return value