from django.contrib import admin
from users.views import GoogleLogin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from .api_root_view import ApiRootView
from dj_rest_auth.registration.views import VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRootView.as_view(), name='api_root'),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('resend-email/', ResendEmailVerificationView.as_view(),name="rest_resend_email"),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email',),
    path('account-email-verification-sent/', TemplateView.as_view(),name='account_email_verification_sent',),
    path('user/login/google/', GoogleLogin.as_view(), name='google_login'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
]
