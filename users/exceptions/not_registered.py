from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException


class AccountNotRegisteredException(APIException):
    status_code = 404
    default_detail = _('The account is not registered.')
    default_code = 'non-registered-account'
