from django.shortcuts import render


def landing_page(request):
    context = {
        "header_title": "Priority Labs | Analytics Platform",
        "header_subtitle": "Data Analytics • Monitoring • Cybersecurity Training",
    }

    return render(request, "main/landing_page.html", context)


def home(request):
    return render(request, "main/home.html")