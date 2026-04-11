from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from .models import Book 

def insert_books(request):
    obj1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.0, edition=3)
    obj1.save() 
    
    obj2 = Book(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price=97.0, edition=2)
    obj2.save() 
    
    obj3 = Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.0, edition=4)
    obj3.save() 
    
    return HttpResponse("Three books have been inserted successfully!")

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook}
    return render(request, 'bookmodule/show.html', context)



def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def view_one_book(request):
    return render(request, 'bookmodule/one_book.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing(request): 
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            
            if contained: newBooks.append(item)
        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks = Book.objects.filter(author__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


    
def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html') 
