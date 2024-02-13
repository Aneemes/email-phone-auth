from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException

class InvalidCredentialsException(APIException):
    status_code = 401
    default_detail = _('Wrong username or password.')
    default_code = 'invalid-credentials'