from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


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


def custom_logout(request):
    logout(request)
    return render(request, "users/auth/logout.html")


@login_required
def profile(request):
    context = {
        "header_title": "Priority Labs | Profile",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "users/account/profile.html", context)