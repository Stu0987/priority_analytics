from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CustomAuthenticationForm, CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:home")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
        "header_title": "Priority Labs | Signup",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "users/auth/signup.html", context)

def login_view(request):
    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST":
        form = CustomAuthenticationForm(
            request=request,
            data=request.POST,
        )

        if form.is_valid():
            login(request, form.get_user())

            if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)

            return redirect("main:home")
    else:
        form = CustomAuthenticationForm(request=request)

    context = {
        "form": form,
        "next": next_url,
        "header_title": "Priority Labs | Login",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "users/auth/login.html", context)

def custom_logout(request):
    logout(request)

    context = {
        "header_title": "Priority Labs | Log Out",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "users/auth/logout.html", context)


@login_required
def profile(request):
    context = {
        "header_title": "Priority Labs | Profile",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "users/account/profile.html", context)

class CustomPasswordResetView(PasswordResetView):
    template_name = "users/auth/password_reset_form.html"
    email_template_name = "users/emails/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")

    extra_context = {
        "header_title": "Priority Labs | Password Reset",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/auth/password_reset_done.html"

    extra_context = {
        "header_title": "Priority Labs | Password Reset",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/auth/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")

    extra_context = {
        "header_title": "Priority Labs | Password Reset",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/auth/password_reset_complete.html"

    extra_context = {
        "header_title": "Priority Labs | Password Reset",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "users/auth/password_change_form.html"
    success_url = reverse_lazy("users:password_change_done")

    extra_context = {
        "header_title": "Priority Labs | Change Password",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "users/auth/password_change_done.html"

    extra_context = {
        "header_title": "Priority Labs | Password Changed",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }