from django.urls import path
from Company import views
app_name = "Company"

urlpatterns = [
 path('Profile/',views.Profile,name="Profile"),
 path('EditProfile/',views.EditProfile,name="EditProfile"),
 path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
 path('HomePage/',views.HomePage,name="HomePage"),
path('Complaint/',views.Complaint,name="Complaint"), 
path('FeedBack/',views.FeedBack,name="FeedBack"),
path('Booking/',views.Booking,name="Booking"),


path('ViewScrap/',views.ViewScrap,name="ViewScrap"),
path('sendrequest/<int:id>',views.sendrequest,name="sendrequest"),

path("payment/<int:id>",views.payment,name="payment"),
path('loader/',views.loader, name='loader'),
path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

path('collectscarp/<int:id>',views.collectscarp, name='collectscarp'),

path('addproduct/',views.addproduct, name='addproduct'),
path('deleteproduct/<int:id>',views.deleteproduct, name='deleteproduct'),
path('addstock/<int:id>',views.addstock, name='addstock'),
path('deletestock/<int:id>/<int:pid>',views.deletestock, name='deletestock'),

path('viewproduct/',views.viewproduct, name='viewproduct'),   
path('Addcart/<int:pid>',views.Addcart, name='Addcart'),   
path('Mycart/',views.Mycart, name='Mycart'),   
path("DelCart/<int:did>", views.DelCart,name="delcart"),
path("CartQty/", views.CartQty,name="cartqty"),

path("productpayment/", views.productpayment,name="productpayment"),
path("mybooking/", views.mybooking,name="mybooking"),
path("reproductpayment/<int:id>", views.reproductpayment,name="reproductpayment"),
path("myproducts/<int:id>", views.myproducts,name="myproducts"),

path('rating/<int:mid>',views.rating,name="rating"),  
path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
path('starrating/',views.starrating,name="starrating"),

path('logout/',views.logout,name="logout"),

]
