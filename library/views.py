from django.shortcuts import render

from django.views.generic import ListView
from django.http import HttpResponseRedirect

from django.db.models import Q

from .models import Book, Author
from .generate_navbar import generate_navbar
from library.Forms.BookSearch import SearchForm

# Create your views here.
def home(request):
    navbar = generate_navbar("home")
    top_books = Book.objects.all().order_by("-rating")
    context = {"navbar": navbar, "top_books": top_books[0:11]}
    return render(request, 'home.html', context=context)


def book_search(request):
    navbar = generate_navbar("test")
    # if this is a POST request we need to process the form data
    if request.method == 'GET' and request.GET.get('title'):
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            query = request.GET.get('title')
            object_list = Book.objects.filter(
                Q(title__icontains=query)
            )
            # print(object_list)
            if len(object_list) == 0:
                object_list = None
            # redirect to a new URL:
            context = {"navbar": navbar, "data": object_list}
            return render(request, 'book_search.html', context=context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {"navbar": navbar, "form": form, "data": "THISISNOTDATA"}
    return render(request, 'book_search.html', context=context)
