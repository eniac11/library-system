from django.urls import path
from library.Views import home, Detail, Search, Series


urlpatterns = [
    path("", home, name="library-home"),
    path("book/search", Search.SearchView.as_view(), name="book-search"),
    path("book/<int:pk>", Detail.DetailView.as_view(), name = "book_detail"),
    path("book/series", Series.ListView.as_view(), name="series_list"),
    path("book/series/<int:pk>", Series.DetailView.as_view(), name="series_detail")
]
