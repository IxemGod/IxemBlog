from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author =  models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=400)
    slug = models.CharField(max_length=100)


    def __str__(self):
        # Ici c'est pour afficher le titre au lieu de 'Object' dans le backoffice
        return self.title

