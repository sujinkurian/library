from django.urls import path
from Webapp import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('Aboutus/',views.Aboutus,name="Aboutus"),
    path('Contact_us/',views.Contact_us,name="Contact_us"),
    path('Contact_add/',views.Contact_add,name="Contact_add"),
    path('product/',views.product,name="product"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('filter_pro/<cat_name>/',views.filter_pro,name="filter_pro"),
    path('reg_pg/',views.reg_pg,name="reg_pg"),
    path('',views.login,name="login"),
    path('add_sign/',views.add_sign,name="add_sign"),
    path('sign/',views.sign,name="sign"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('add_cart/',views.add_cart,name="add_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('cart_del/<int:cart_id>',views.cart_del,name="cart_del"),
    path('checkout/',views.checkout,name="checkout"),
    path('payment/',views.payment,name="payment"),
    path('checkout_payment/',views.checkout_payment,name="checkout_payment"),
]