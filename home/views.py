from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Article

from .forms import ValidateAddArticle
from .forms import NameForm

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

def name(request):
    return render(request, "home/name.html")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['your_name']
            # redirect to a new URL:
            data = {"name" : name}
            return render(request, "home/result.html", data)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})

def validate_add_article(request):
   if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ValidateAddArticle(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            picture = form.cleaned_data['picture']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            slug = form.cleaned_data['slug']

            Article.objects.create(title=title, body=content, author=author, image=picture, slug=slug)

            return HttpResponseRedirect(f"/blog/article/{slug}")
        else:
            form = ValidateAddArticle()

        return render(request, "home/index.html", {"form": form})
