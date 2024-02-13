from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ApiRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            'login': reverse('users:user_login', request=request, format=format),
            'register': reverse('users:user_register', request=request, format=format),
            'send_sms': reverse('users:send_resend_sms', request=request, format=format),
            'verify_phone': reverse('users:verify_phone_number', request=request, format=format),
            'google_login': reverse('google_login', request=request, format=format),
            'password_reset': reverse('rest_password_reset', request=request, format=format),
            'password_change': reverse('rest_password_change', request=request, format=format),
            'logout': reverse('rest_logout', request=request, format=format),
            'resend_email': reverse('rest_resend_email', request=request, format=format),
            'account_email_verification_sent': reverse('account_email_verification_sent', request=request, format=format),
        })