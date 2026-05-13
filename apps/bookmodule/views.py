from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Sum, Avg, Max, Min, Count, F, FloatField, ExpressionWrapper
from .models import Book, Publisher, Author, Address, Student, Student2, Address2
from .forms import BookForm, StudentForm, StudentForm2
from .forms import StudentProfileForm
from .models import StudentProfile
from django.contrib.auth.decorators import login_required 

@login_required(login_url='/users/login/')  #task4

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/student_form.html', {'form': form, 'title': 'Add Student'})

def update_student(request, id):
    student = Student.objects.get(id=id) 
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list_students')
    return render(request, 'bookmodule/student_form.html', {'form': form, 'title': 'Update Student'})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list_students')

def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = StudentForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = StudentForm2()
    return render(request, 'bookmodule/student_form.html', {'form': form})



def add_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponse("Image Uploaded Successfully!")
    else:
        form = StudentProfileForm()
    return render(request, 'bookmodule/add_profile.html', {'form': form})

def lab10_listbooks(request):
    books = Book.objects.all() 
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

def lab10_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        new_book = Book(title=title, author=author)
        new_book.save()
        return redirect('lab10_listbooks')
    
    return render(request, 'bookmodule/lab10_addbook.html')

def lab10_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab10_listbooks')


def lab10_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save() 
        return redirect('lab10_listbooks')
    
    return render(request, 'bookmodule/lab10_editbook.html', {'obj': book})




## part2 

def lab10_listbooks_p2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks_p2.html', {'books': books})

def lab10_addbook_p2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('lab10_listbooks_p2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_addbook_p2.html', {'form': form})

def lab10_editbook_p2(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) 
        if form.is_valid():
            form.save()
            return redirect('lab10_listbooks_p2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_editbook_p2.html', {'form': form})

def lab10_deletebook_p2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab10_listbooks_p2')
















def task1(request):
    books = Book.objects.filter(Q(price__lte=80)) 
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task3(request):
   
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    ) 
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookStats.html', {'stats': stats})

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/cityStats.html', {'cities': cities})

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

# Lab 9 Tasks: Advanced Aggregation & Annotation

def lab9_task1(request):
    
    books = Book.objects.annotate(
        availability=ExpressionWrapper(F('quantity') * 1.0 / 100 * 100, output_field=FloatField())
    )
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_p=Avg('book__price'), 
        min_p=Min('book__price'), 
        max_p=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    publishers = Publisher.objects.filter(book__rating__gt=4).annotate(high_rated_count=Count('book'))
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    
    publishers = Publisher.objects.filter(
        book__price__gt=50, 
        book__quantity__lt=5, 
        book__quantity__gte=1
    ).annotate(total_books=Count('book'))
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})