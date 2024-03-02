from django.shortcuts import render


def home_page(request):
    context = {
        "title": "home_page"
    }

    return render(request, "common/index.html", context)


def about(request):
    context = {}

    return render(request, "common/about.html", context)