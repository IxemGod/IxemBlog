from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    data = {"articles" : articles}
    return render(request, "home/index.html", data)