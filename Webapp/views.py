from django.shortcuts import render,redirect
from Webapp.models import Contact_db,Sign_up,Cart_db,Order_db
from Textapp.models import category_db,product_db
from django.contrib.auth import authenticate,login
from django.contrib import messages
import razorpay
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    cat = category_db.objects.all()
    return render(request,"Home.html",{'cat':cat})
def Aboutus(request):
    cat = category_db.objects.all()
    return render(request,"About_us.html",{'cat':cat})
def Contact_us(request):
    cat = category_db.objects.all()
    return render(request,"Contact.html",{'cat':cat})
def Contact_add(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ms = request.POST.get('message')
        obj = Contact_db(Name=na,Email_Id=em,Message=ms)
        obj.save()
        return redirect('Contact_us')

def product(request):
    cat = category_db.objects.all()
    products = product_db.objects.all()
    return render(request,"All_product.html",{'products':products,'cat':cat})
def single_product(request,pro_id):
    product = product_db.objects.get(id=pro_id)
    return render(request, "Single_product.html", {'product': product})
def filter_pro(request,cat_name):
    data = product_db.objects.filter(Category_name=cat_name)   #like id=data.id
    return render(request,"Filtered_product.html",{'data':data})

def reg_pg(request):
    return render(request,"Registration.html")

def login(request):
    return render(request,"login.html")
def add_sign(request):
    if request.method == "POST":
        na = request.POST.get('user_name')
        em = request.POST.get('email')
        pas = request.POST.get('pass')
        img1 = request.FILES['pro_img1']
        obj = Sign_up(Username=na, Email_Id=em, Password=pas,Profile_image=img1)
        obj.save()
        return redirect('reg_pg')

def sign(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if Sign_up.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            return redirect('homepage')
        else:
            return redirect('login')
    else:
        return redirect('login')

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect('homepage')

def add_cart(request):
    if request.method == "POST":
        na = request.POST.get('qt')
        pt = request.POST.get('price')
        em = request.POST.get('Username')
        pn = request.POST.get('product_name')
        tp = request.POST.get('total_price')
        obj = Cart_db(User_Name=em,Product_Name=pn,Quantity=na,Price=pt,Total_Price=tp)
        obj.save()
        messages.success(request,"Product added to cart Succesfully")
        return redirect('homepage')

def cart_page(request):
    data = Cart_db.objects.filter(User_Name=request.session['Username'])
    cat = category_db.objects.all()
    sub_total = 0
    total=0
    shipping=0
    for i in data:
        sub_total += i.Total_Price
        if sub_total>3000:
            shipping = 150
        else:
            shipping = 250
        total = sub_total+shipping
    return render(request,"Cart.html",{'data': data ,'cat':cat,'sub_total':sub_total,'shipping':shipping,'total':total})
def cart_del(request,cart_id):
    x = Cart_db.objects.filter(id=cart_id)
    x.delete()
    messages.success(request,"Iteam Got deleted")
    return redirect('cart_page')
def checkout(request):
    data = Cart_db.objects.filter(User_Name=request.session['Username'])
    sub_total = 0
    total = 0
    shipping = 0
    for i in data:
        sub_total += i.Total_Price
        if sub_total > 3000:
            shipping = 150
        else:
            shipping = 250
        total = sub_total + shipping
    return render(request,"Checkout.html",{'data':data,'sub_total':sub_total,'shipping':shipping,'total':total})

def checkout_payment(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pl = request.POST.get('place')
        ad = request.POST.get('address')
        mo = request.POST.get('mobile')
        ms = request.POST.get('Message')
        tp = request.POST.get('total_price')
        obj = Order_db(Name=na,Email=em,Place=pl,Totalprice=tp,Address=ad,Mobile=mo,Message=ms)
        obj.save()
        messages.success(request,"Proceed to payament succesfully")
        return redirect('payment')

def payment(request):
    #retrive the order objects with specific id
    customer=Order_db.objects.order_by('-id').first()
    #
    payy=customer.Totalprice
    amount=int(payy*100)
    payy_str=str(amount)
    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_K6d0cwxZVUtEm4','ziMIawzteOKAeZq0vAhHSfEY'))
        payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})


