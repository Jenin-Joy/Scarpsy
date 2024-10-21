from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('LoginForm/',views.LoginForm,name="LoginForm"),
    path('SignUpForm/',views.SignUpForm,name="SignUpForm"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),   
    path('Shop/',views.Shop,name="Shop"),
    path('company/',views.company,name="company"),
    path('',views.index,name="index"),
    






]