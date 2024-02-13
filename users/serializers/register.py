from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from users.models import PhoneNumber

User = get_user_model()

class UserRegistrationSerializer(RegisterSerializer):
    """
    Serializer for registrating new users using email or phone number.
    """
    username = None
    phone_number = PhoneNumberField(
        required=False,
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=PhoneNumber.objects.all(),
                message=_(
                    "A user is already registered with this phone number."),
            )
        ],
    )
    email = serializers.EmailField(required=False)

    def validate(self, validated_data):
        email = validated_data.get('email', None)
        phone_number = validated_data.get('phone_number', None)

        if not (email or phone_number):
            raise serializers.ValidationError(
                _("Enter an email or a phone number."))

        if validated_data['password1'] != validated_data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))

        return validated_data

    def get_cleaned_data_extra(self):
        return {
            'phone_number': self.validated_data.get('phone_number', ''),
        }

    def create_phone(self, user, validated_data):
        phone_number = validated_data.get("phone_number")

        if phone_number:
            PhoneNumber.objects.create(user=user, phone_number=phone_number)
            user.phone.save()

    def custom_signup(self, request, user):
        self.create_phone(user, self.get_cleaned_data_extra())