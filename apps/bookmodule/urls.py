from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('list_books/', views.list_books, name="books.list_books"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name='books.links'), 
    path('html5/text/formatting/', views.text_formatting, name='books.text_formatting'),
    path('html5/listing/', views.listing, name='books.listing'),
    path('html5/tables/', views.tables, name='books.tables'),

    path('simple/query/', views.simple_query),  
    path('lab7/insert_books/', views.insert_books),
    path('complex/query/', views.complex_query, name='complex_query'),
]