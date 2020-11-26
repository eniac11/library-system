from django.views.generic import ListView as LV
from django.views.generic import DetailView as DV
from library.models import Series
from django import forms
from django.contrib.admin import widgets  

class ListView(LV):
    model = Series
    template_name = "series_list.html"
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "book"
        return context

class DetailView(DV):
    model = Series
    template_name = "series_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "book"
        return context