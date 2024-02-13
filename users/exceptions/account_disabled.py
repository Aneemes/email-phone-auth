from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException

class AccountDisabledException(APIException):
    status_code = 403
    default_detail = _('The account is disabled.')
    default_code = 'account-disabled'
