from django.shortcuts import render


def blog_view(request):
    context = {}

    return render(request, "blog/list_articles.html")


def article_view(request):
    context = {}

    return render(request, "blog/details_article.html")