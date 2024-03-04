from django.shortcuts import render


def blog_view(request):
    context = {}

    return render(request, "blog/blog_all_articles.html")
