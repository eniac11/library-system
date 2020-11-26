from django import forms

SearchOptions = [
    ('title', 'Title'),
    ('isbn', 'ISBN'),
]

class SearchForm(forms.Form):
    search_request = forms.CharField(label='Book', widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=100)
    # add a css class to search type for styling
    search_type = forms.CharField(label="Part of Book", widget=forms.Select(choices=SearchOptions, attrs={'class' : 'form-control'}))