from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def landing_page(request):
    context = {
        "header_title": "Priority Labs | Analytics Platform",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
        "show_landing_header": True,
    }

    return render(request, "main/landing_page.html", context)

@login_required
def home(request):
    context = {
            "header_title": "Home | Priority/Analytics",
            "header_subtitle": "Dashboard foundation",
        }
    return render(request, "main/home.html", context)