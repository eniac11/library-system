from django.views.generic.detail import DetailView as DV
from library.models import Book
from django import forms
from django.contrib.admin import widgets                                       

class ProductForm(forms.ModelForm):
    class Meta:
        model = Book
    
        fields = {
            'published_date':  widgets.AdminDateWidget()
        }

class DetailView(DV):
    model = Book
    template_name = "book_detail.html"
    form = ProductForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "book"
        return context