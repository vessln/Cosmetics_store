from django.shortcuts import render


def home_page(request):
    context = {
        "title": "home page"
    }

    return render(request, "common/home_page.html", context)


def about(request):

    return render(request, "common/about.html")