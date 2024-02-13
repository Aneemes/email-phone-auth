from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from users.exceptions.not_registered import AccountNotRegisteredException
from users.models import PhoneNumber

User = get_user_model()

class VerifyPhoneNumberSerialzier(serializers.Serializer):
    """
    Serializer class to verify OTP.
    """
    phone_number = PhoneNumberField()
    otp = serializers.CharField(max_length=settings.TOKEN_LENGTH)

    def validate_phone_number(self, value):
        queryset = User.objects.filter(phone__phone_number=value)
        if not queryset.exists():
            raise AccountNotRegisteredException()
        return value

    def validate(self, validated_data):
        phone_number = str(validated_data.get('phone_number'))
        otp = validated_data.get('otp')

        queryset = PhoneNumber.objects.get(phone_number=phone_number)

        queryset.check_verification(security_code=otp)

        return validated_data