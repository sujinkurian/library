from django.shortcuts import render, redirect
from libapp.models import student_db, book_db, registraion_db


# Create your views here.
def lib_page(request):
    return render(request, "lib.html")


def student_page(request):
    return render(request, "Add_student.html")

def display_stud(request):
    data = student_db.objects.all()
    return render(request,"student_details.html",{'data':data})

def student_details(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        ag = request.POST.get('Age')
        mo = request.POST.get('Mobile')
        em = request.POST.get('Email')
        ad = request.POST.get('address')
        co = request.POST.get('course')
        ge = request.POST.get('gender')
        obj = student_db(Name=na, Age=ag, Mobile=mo, Email=em, Address=ad, Course=co, Gender=ge)
        obj.save()
        return redirect('student_page')
def book_page(request):
    return render(request,"Add_book.html")
def add_book(request):
    if request.method == "POST":
        bn = request.POST.get('BookName')
        an = request.POST.get('Authorname')
        pr = request.POST.get('Price')
        pd = request.POST.get('Publishdate')
        obj = book_db(BookName=bn,Authorname=an,Price=pr,Publishdate=pd)
        obj.save()
        return redirect('book_page')
def display_book(request):
    da = book_db.objects.all()
    return render(request,"book_details.html",{'data' : da})
def edit_student(request,stud_id):
    data = student_db.objects.get(id=stud_id)
    return render(request,"edit_student.html",{'data':data})
def update_book(request,book_id):
    if request.method == "POST":
        bn = request.POST.get('BookName')
        an = request.POST.get('Authorname')
        pr = request.POST.get('Price')
        pd = request.POST.get('Publishdate')
        book_db.objects.filter(book_id).update(BookName=bn,Authorname=an,Price=pr,Publishdate=pd)
        return redirect('book_page')
def add_emp(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mo = request.POST.get('mobile')
        pl  = request.POST.get('place')
        img  = request.FILES['image']
        obj = registraion_db(Name=na,Mobile=mo,Place= pl,Profileimage=img)
        obj.save()
    return render(request,"registration.html")


