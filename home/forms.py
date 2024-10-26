from django import forms

class ValidateAddArticle(forms.Form):
    title = forms.CharField(label = "title", max_length=400)
    picture = forms.CharField(label = "picture", min_length=4)
    content = forms.CharField(label = "content", min_length=4)
    author = forms.CharField(label = "author", min_length=4)
    slug = forms.CharField(label = "slug", min_length=4)


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class Search(forms.Form):
    search = forms.CharField(label="Requête", min_length=1)