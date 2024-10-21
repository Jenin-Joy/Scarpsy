from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [

    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePswd/',views.ChangePswd,name="ChangePswd"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('Scrap/',views.Scrap,name="Scrap"),
    path('delscrap/<int:id>',views.delscrap,name="delscrap"),  
    path('Complaint/',views.Complaint,name="Complaint"),
    path('FeedBack/',views.FeedBack,name="FeedBack"),
    path('MyScrap/',views.MyScrap,name="MyScrap"),
    path('View_Booking/',views.viewbooking,name="viewbooking"),
    path('verifyrequest/<int:id>/<int:status>',views.verifyrequest,name="verifyrequest"),
    path('logout/',views.logout,name="logout"),


]