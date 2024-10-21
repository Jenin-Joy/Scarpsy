from django.urls import path
from Shop import views
app_name = "Shop"

urlpatterns = [

    path('Profile/',views.Profile,name="Profile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('ViewScrap/',views.ViewScrap,name="ViewScrap"),
    path('delViewScrap/<int:id>',views.delViewScrap,name="delViewScrap"), 
    path('Complaint/',views.Complaint,name="Complaint"), 
    path('FeedBack/',views.FeedBack,name="FeedBack"),
    path('sendrequest/<int:id>',views.sendrequest,name="sendrequest"),
    path('viewbooking/',views.viewbooking,name="viewbooking"),
    
    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path('AddScrap/',views.AddScrap, name='AddScrap'),

    path('collectscarp/<int:id>',views.collectscarp, name='collectscarp'),

    path('delscrap/<int:id>',views.delscrap,name="delscrap"),
    path('companybooking/',views.companybooking,name="companybooking"),
    path('verifyrequest/<int:id>/<int:status>',views.verifyrequest,name="verifyrequest"),

    path('logout/',views.logout,name="logout"),


]
