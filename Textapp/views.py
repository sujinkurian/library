import datetime
from django.shortcuts import render,redirect
from Textapp.models import category_db,product_db
from Webapp.models import Contact_db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    today = datetime.datetime.now()
    return render(request,"index.html",{'today':today})
def demo_pg(request):
    return render(request,"Demo.html")
def cat_page(request):
    today = datetime.datetime.now()
    return render(request,"add_category.html",{'today':today})
def cat_dis(request):
    da = category_db.objects.all()
    return render(request,"view_category.html",{'data': da})
def add_cat(request):
    if request.method == "POST":
        na = request.POST.get('cname')
        dn = request.POST.get('description')
        img = request.FILES['cat_img']
        obj = category_db(Name=na,Description=dn,Cat_image=img)
        obj.save()
        messages.success(request,"Category saves succesfully")
        return redirect('cat_page')
def edit_cat(request,cat_id):
    data = category_db.objects.get(id=cat_id)
    return render(request,"edit_cat.html",{'data':data})
def update_cat(request,cat_id):
    if request.method == "POST":
        na = request.POST.get('name')
        dn = request.POST.get('description')
        try:
            img = request.FILES['cat_img']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=cat_id).Cat_image
        category_db.objects.filter(id=cat_id).update(Name=na,Description=dn,Cat_image=file)
        return redirect('cat_dis')
def pro_page(request):
    category = category_db.objects.all()
    return render(request,"add_product.html",{'category':category},)
def add_pro(request):
    if request.method == "POST":
        na = request.POST.get('cname')
        pn = request.POST.get('product_name')
        dn = request.POST.get('description')
        pc = request.POST.get('price')
        bd = request.POST.get('brand')
        img1 = request.FILES['pro_img1']
        img2 = request.FILES['pro_img2']
        img3 = request.FILES['pro_img3']
        obj = product_db(Category_name=na,Product_name=pn,Description=dn,Price=pc,Brand=bd,Profile_img1=img1,Profile_img2=img2,Profile_img3=img3)
        obj.save()
        messages.success(request,"Product saved succesfully")
        return redirect('pro_page')
def dis_pro(request):
    da = product_db.objects.all()
    return render(request, "view_product.html", {'data': da})
def edit_pro(req,pro_id):
    cat = category_db.objects.all()
    products = product_db.objects.get(id=pro_id)
    return render(req,"edit_pro.html",{'cat':cat,'products':products})
def update_pro(request,pro_id):
    if request.method == "POST":
        na = request.POST.get('cname')
        pn = request.POST.get('product_name')
        dn = request.POST.get('description')
        pc = request.POST.get('price')
        bd = request.POST.get('brand')
        try:
            img1 = request.FILES['cat_img1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1 = product_db.objects.get(id=pro_id).Profile_img1
        try:
            img2 = request.FILES['cat_img2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = product_db.objects.get(id=pro_id).Profile_img2
        try:
            img3 = request.FILES['cat_img3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = product_db.objects.get(id=pro_id).Profile_img3
        product_db.objects.filter(id=pro_id).update(Category_name=na,Product_name=pn,Description=dn,Price=pc,Brand=bd,Profile_img1=file1,Profile_img2=file2,Profile_img3=file3)
        messages.success(request,"Updated succesfully")
        return redirect('dis_pro')

def admin_login_page(request):
    return render(request,"admin_login.html")
def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request,"Welcome ANd have a good day")
                return redirect(index)
            else:
                messages.warning(request,"Invalid password")
                return redirect(admin_login_page)
        else:
            messages.warning(request,"INvalid user or password")
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('admin_login_page')

def contact_details(request):
    da = Contact_db.objects.all()
    return render(request, "contact_details.html", {'data': da})

