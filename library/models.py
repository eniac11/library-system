from django.db import models
from django.urls import reverse


# # Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.last_name is not None:
            return ' '.join([self.first_name, self.last_name])
        else:
            return self.first_name

    class Meta:
        ordering = ["last_name"]


class Series(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField("Book")

    def get_absolute_url(self):
        return reverse('library:series_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
    def get_books(self):
        for book in self.books.all():
            yield book

class Book(models.Model):
    title = models.CharField(max_length=255)
    total_pages = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    isbn = models.CharField(max_length=13, verbose_name="ISBN", null=True)
    published_date = models.DateField(null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre)
    blurb = models.CharField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum", max_length=444)
    series_ref = models.ForeignKey(Series, models.CASCADE, null=True)
    
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={"pk": self.pk})

    class Meta:
        ordering = ["title"]

