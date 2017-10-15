from django.db import models

# Create your models here.

class Author(models.Model):
    authorid = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author)
    publisher = models.CharField(max_length=30)
    publishdate = models.DateTimeField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.title
