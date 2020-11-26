from django.shortcuts import render

from django.db.models import Q

from django.views.generic.detail import DetailView
from library.models import Book
from library.Forms.BookSearch import SearchForm

from library.generate_navbar import generate_navbar

class SearchView(DetailView):
    model = Book
    template_name = "book_search.html"
    
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if form.is_valid():
            search_request = form.cleaned_data["search_request"]
            search_type = form.cleaned_data["search_type"]
            print(search_request)
            print(search_type)
            if search_type == "title":
                object_list = Book.objects.filter(
                    Q(title__icontains=search_request)
                )
            if search_type == "isbn":
                object_list = Book.objects.filter(
                    Q(isbn__icontains=search_request)
                )
            
            if len(object_list) == 0:
                object_list = None

            context = {"data": object_list, "form": form}
            context['navbar'] = generate_navbar('')
            return render(request, 'book_search.html', context=context)
        
        context = { "data": "THISISNOTDATA", "form": SearchForm()}
        context['navbar'] = generate_navbar('')
        return render(request, 'book_search.html', context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = generate_navbar('')
        print(context['navbar'])
        return context


def book_search(request):
    navbar = generate_navbar("")
    # if this is a POST request we need to process the form data
    if request.method == 'GET' and request.GET.get('title'):
        # create a form instance and populate it with data from the request:
        new_search_form = SearchForm()
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
            context = {"navbar": navbar, "data": object_list, "form": new_search_form}
            return render(request, 'book_search.html', context=context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {"nbar": "book", "form": form, "data": "THISISNOTDATA"}
    return render(request, 'book_search.html', context=context)