from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .forms import CustomAuthenticationForm

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "",
        auth_views.LoginView.as_view(
            template_name="users/auth/login.html",
            authentication_form=CustomAuthenticationForm,
            extra_context={
                "header_title": "Priority Labs | Login",
                "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
            },
        ),
        name="login",
    ),
    path("logout/", views.custom_logout, name="logout"),
    path("profile/", views.profile, name="profile"),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/auth/password_reset_form.html",
            email_template_name="users/emails/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/auth/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/auth/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/auth/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),

    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/auth/password_change_form.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/auth/password_change_done.html",
        ),
        name="password_change_done",
    ),
]