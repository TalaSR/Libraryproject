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
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'), 
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab9/task1', views.lab9_task1), 
    path('lab9/task2', views.lab9_task2),  
    path('lab9/task3', views.lab9_task3),
    path('lab9/task4', views.lab9_task4),
    path('lab9/task5', views.lab9_task5),
    path('lab9/task6', views.lab9_task6),

    path('lab9_part1/listbooks', views.lab10_listbooks, name='lab10_listbooks'),
    path('lab9_part1/addbook', views.lab10_addbook, name='lab10_addbook'),
    path('lab9_part1/editbook/<int:id>', views.lab10_editbook, name='lab10_editbook'),
    path('lab9_part1/deletebook/<int:id>', views.lab10_deletebook, name='lab10_deletebook'),

    path('lab9_part2/listbooks', views.lab10_listbooks_p2, name='lab10_listbooks_p2'),
    path('lab9_part2/addbook', views.lab10_addbook_p2, name='lab10_addbook_p2'),
    path('lab9_part2/editbook/<int:id>', views.lab10_editbook_p2, name='lab10_editbook_p2'),
    path('lab9_part2/deletebook/<int:id>', views.lab10_deletebook_p2, name='lab10_deletebook_p2'),

   # Task 1
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    # Task 2 
    path('students2/', views.list_students2, name='list_students2'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('add_profile/', views.add_profile, name='add_profile'),


   
]

