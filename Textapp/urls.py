from django.urls import path
from Textapp import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('demo_pg/',views.demo_pg,name="demo_pg"),
    path('cat_page/',views.cat_page,name="cat_page"),
    path('add_cat/',views.add_cat,name="add_cat"),
    path('cat_dis/',views.cat_dis,name="cat_dis"),
    path('edit_cat/<int:cat_id>',views.edit_cat,name="edit_cat"),
    path('update_cat/<int:cat_id>',views.update_cat,name="update_cat"),
    path('pro_page/',views.pro_page,name="pro_page"),
    path('add_pro/',views.add_pro,name="add_pro"),
    path('dis_pro/',views.dis_pro,name="dis_pro"),
    path('edit_pro/<int:pro_id>/',views.edit_pro,name="edit_pro"),
    path('update_pro/<int:pro_id>/',views.update_pro,name="update_pro"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_details/',views.contact_details,name="contact_details")
]
