from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    data = {"articles" : articles}
    return render(request, "home/index.html", data)

def single_article(request, slug):
    article = Article.objects.get(slug=slug)
    data = {'article' : article}
    return render(request, "home/article.html", data)

def add_article(request):
    return render(request, "home/add.html")