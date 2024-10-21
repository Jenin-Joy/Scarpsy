from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    
    path('District/',views.District,name="District"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),  
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
    
    path('Category/',views.Category,name="Category"),
    path('delcategory/<int:id>',views.delcategory,name="delcategory"),  
    path('editcategory/<int:id>',views.editcategory,name="editcategory"),

    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsubcategory/<int:id>',views.delsubcategory,name="delsubcategory"),  
    path('editsubcategory/<int:id>',views.editsubcategory,name="editsubcategory"), 

    path('Registration/',views.Registration,name="Registration"),  
    path('delRegistration/<int:id>',views.delRegistration,name="delRegistration"),  
    path('editRegistration/<int:id>',views.editRegistration,name="editRegistration"),

    path('Place/',views.Place,name="Place"),     
    path('delPlace/<int:id>',views.delPlace,name="delPlace"),  
    path('editPlace/<int:id>',views.editPlace,name="editPlace"),
    path('HomePage/',views.HomePage,name="HomePage"),  

    path('newshop/',views.newshop,name="newshop"),  
    path('verifyshop/<int:id>/<int:status>',views.verifyshop,name="verifyshop"),  
    path('approvedshop/',views.approvedshop,name="approvedshop"),  
    path('rejectedshop/',views.rejectedshop,name="rejectedshop"), 

    path('newcompany/',views.newcompany,name="newcompany"),  
    path('verifycompany/<int:id>/<int:status>',views.verifycompany,name="verifycompany"),  
    path('approvedcompany/',views.approvedcompany,name="approvedcompany"),  
    path('rejectedcompany/',views.rejectedcompany,name="rejectedcompany"),  

    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),  
    path('reply/<int:id>',views.reply,name="reply"),  
    path('replyedcomplaint/',views.replyedcomplaint,name="replyedcomplaint"),  
    path('logout/',views.logout,name="logout"),

]
