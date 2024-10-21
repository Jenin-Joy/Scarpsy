from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Shop.models import *
# Create your views here.

def HomePage(request):
   if "uid" in request.session:
      return render(request,'User/HomePage.html') 
   else:
      return redirect("Guest:LoginForm")

def logout(request):
    del request.session["uid"]
    return redirect("Guest:LoginForm")

def MyProfile(request):
   if "uid" in request.session:
      user=tbl_user.objects.get(id=request.session['uid'])
      return render(request,'User/MyProfile.html',{'user':user})
   else:
      return redirect("Guest:LoginForm")

def EditProfile(request):
   if "uid" in request.session:
      user=tbl_user.objects.get(id=request.session['uid'])
      if request.method == "POST":
         user.User_Name = request.POST.get("name")
         user.User_Address = request.POST.get("txtaddress")
         user.User_Contact = request.POST.get("contact")
         user.User_Email = request.POST.get("email")
         user.save()
         return render(request,'User/EditProfile.html',{'msg':"Profile Updated"})
      else:
         return render(request,'User/EditProfile.html',{'user':user})
   else:
      return redirect("Guest:LoginForm")



def ChangePswd(request):
   if "uid" in request.session:
      user=tbl_user.objects.get(id=request.session['uid'])
      if request.method == "POST":
         if user.User_Password == request.POST.get("old"):
            if request.POST.get("new") == request.POST.get("retype"):
               user.User_Password = request.POST.get("retype")
               user.save()
               return render(request,'User/ChangePswd.html',{"msg":"Profile Updated"})
            else:
               return render(request,'User/ChangePswd.html',{"msg1":"Error In Re Password"})
         else:
            return render(request,'User/ChangePswd.html',{"msg1":"Error In Old Password"})
      else:
         return render(request,'User/ChangePswd.html')
   else:
      return redirect("Guest:LoginForm")


   
def Scrap(request):
   if "uid" in request.session:
      cat=tbl_category.objects.all()
      scrap = tbl_Scrap.objects.filter(User=request.session["uid"])
      if request.method=="POST":
         Category=request.POST.get('selcategory')
         Quantity=request.POST.get('txtquantity')
         Description=request.POST.get('txtdescription')
         Price=request.POST.get('txtprice')
         Photo=request.FILES.get('txtphoto')
         tbl_Scrap.objects.create( 
         category=tbl_category.objects.get(id=request.POST.get('selcategory')),      
         Scrap_Category=Category,
         Scrap_Quantity=Quantity,
         Scrap_Description=Description,
         Scrap_Price=Price,
         Scrap_Photo=request.FILES.get("txtphoto"),
         User=tbl_user.objects.get(id=request.session["uid"])
         )
         return render(request,'User/Scrap.html',{'msg':"Data Inserted"})
      else:
         return render(request,'User/Scrap.html',{'category':cat,"scrap":scrap})
   else:
      return redirect("Guest:LoginForm")
      
def delscrap(request,id):
    tbl_Scrap.objects.get(id=id).delete()
    return render(request,'User/Scrap.html',{'msg':"Data Deleted"})


def Complaint(request):
   if "uid" in request.session:
      complaint = tbl_Complaint.objects.filter(User=request.session["uid"])
      if request.method=="POST":
         Title=request.POST.get('txttitle')
         Content=request.POST.get('txtcontent')
         User=tbl_user.objects.get(id=request.session["uid"])
         tbl_Complaint.objects.create(       
         Complaint_Title=Title,
         Complaint_Content=Content,
         User=User
         )
         return redirect("User:Complaint")
      else:
         return render(request,'User/Complaint.html',{"complaint":complaint})
   else:
      return redirect("Guest:LoginForm")
      

def FeedBack(request):
   if "uid" in request.session:
      if request.method=="POST":
         Content=request.POST.get('txtcontent')
         tbl_FeedBack.objects.create(       
         Feedback_Content=Content,
         )
         return redirect("User:FeedBack")
      else:
         return render(request,'User/FeedBack.html')
   else:
      return redirect("Guest:LoginForm")

def MyScrap(request):
   if "uid" in request.session:
      return render(request,'User/MyScrap.html')
   else:
      return redirect("Guest:LoginForm")

def viewbooking(request):
   if "uid" in request.session:
      scrap = tbl_shopbooking.objects.filter(scarp__User=request.session["uid"])
      return render(request,"User/View_Booking.html",{"book":scrap})
   else:
      return redirect("Guest:LoginForm")

def verifyrequest(request, id, status):
   booking= tbl_shopbooking.objects.get(id=id)
   booking.shopbooking_status = status
   booking.save()
   scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
   scrap.scarp_status=1
   scrap.save()
   msg =""
   if status == 1:
      msg = "Request Accepted"
   else:
      msg = "Request Rejected"
   return render(request,"User/View_Booking.html" ,{"msg":msg})