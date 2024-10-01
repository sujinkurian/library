from django.urls import path
from libapp import views
urlpatterns = [
    path('lib_page/', views.lib_page,name="lib_page"),
    path('student_page/', views.student_page,name="student_page"),
    path('student_details/', views.student_details,name="student_details"),
    path('display_stud/', views.display_stud,name="display_stud"),
    path('book_page/', views.book_page,name="book_page"),
    path('add_book/', views.add_book,name="add_book"),
    path('display_book/', views.display_book,name="display_book"),
    path('edit_student/<int:stud_id>', views.edit_student,name="edit_student"),
    path('update_book/<int:stud_id>', views.update_book,name="update_book"),
    path('add_emp/', views.add_emp,name="add_emp")
]
