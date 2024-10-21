from django.shortcuts import render,redirect
from Admin.models import *
from Shop.models import *
from Guest.models import *
from User.models import *
from Company.models import *

# Create your views here.
def HomePage(request):
   if "sid" in request.session:
      return render(request,'Shop/HomePage.html')
   else:
      return redirect("Guest:LoginForm")

def logout(request):
    del request.session["sid"]
    return redirect("Guest:LoginForm")

def Profile(request):
   if "sid" in request.session:
      shop=tbl_newShop.objects.get(id=request.session['sid'])
      return render(request,'Shop/Profile.html',{'shop':shop})
   else:
      return redirect("Guest:LoginForm")


def EditProfile(request):
   if "sid" in request.session:
      shop=tbl_newShop.objects.get(id=request.session['sid'])
      if request.method == "POST" :
         shop.Shop_Name = request.POST.get("name")
         shop.Shop_Address = request.POST.get("txtaddress")
         shop.Shop_Contact = request.POST.get("contact")
         shop.Shop_Email = request.POST.get("email")
         shop.save()
         return render(request,'Shop/EditProfile.html',{'msg':"Profile Updated"})
      else:
         return render(request,'Shop/EditProfile.html',{'shop':shop})
   else:
      return redirect("Guest:LoginForm")


def ChangePassword(request):
   if "sid" in request.session:
      shop=tbl_newShop.objects.get(id=request.session['sid'])
      if request.method == "POST":
         if shop.Shop_Password == request.POST.get("old"):
            if request.POST.get("new") == request.POST.get("retype"):
               shop.Shop_Password = request.POST.get("retype")
               shop.save()
               return render(request,'Shop/ChangePswd.html',{"msg":"Profile Updated"})
            else:
               return render(request,'Shop/ChangePswd.html',{"msg1":"Error In Re Password"})
         else:
            return render(request,'Shop/ChangePswd.html',{"msg1":"Error In Old Password"})
      else:
         return render(request,'Shop/ChangePassword.html')
   else:
      return redirect("Guest:LoginForm")


def ViewScrap(request):
   if "sid" in request.session:
      user = tbl_user.objects.all()
      scrap = tbl_Scrap.objects.filter(scarp_status=0,User__in=user)
      return render(request,'Shop/ViewScrap.html',{'scrap':scrap})
   else:
      return redirect("Guest:LoginForm")


def delViewScrap(request,id):
    tbl_ViewScrap.objects.get(id=id).delete()
    return render(request,'Admin/ViewScrap.html',{'msg':"Data Deleted"})

      
def Complaint(request):
   if "sid" in request.session:
      complaint = tbl_Complaint.objects.filter(Shop=request.session["sid"])
      if request.method=="POST":
         Title=request.POST.get('txttitle')
         Content=request.POST.get('txtcontent')
         Company=tbl_newShop.objects.get(id=request.session["sid"])
         tbl_Complaint.objects.create(       
         Complaint_Title=Title,
         Complaint_Content=Content,
         Shop=Shop
         )
         return redirect("Shop:Complaint")
      else:
         return render(request,'Shop/Complaint.html',{"complaint":complaint})
   else:
      return redirect("Guest:LoginForm")


def FeedBack(request):
   if "sid" in request.session:
      if request.method=="POST":
         Content=request.POST.get('txtcontent')
         tbl_FeedBack.objects.create(       
         Feedback_Content=Content,
         )
         return redirect("Shop:FeedBack")
      else:
         return render(request,'Shop/FeedBack.html')
   else:
      return redirect("Guest:LoginForm")
      
def sendrequest(request, id):
   tbl_shopbooking.objects.create(shop=tbl_newShop.objects.get(id=request.session["sid"]),scarp=tbl_Scrap.objects.get(id=id))
   return render(request,"Shop/ViewScrap.html",{"msg":"Request Sended"})

def viewbooking(request):
   if "sid" in request.session:
      booking = tbl_shopbooking.objects.filter(shop=request.session["sid"])
      return render(request,"Shop/View_Booking.html",{"booking":booking})
   else:
      return redirect("Guest:LoginForm")

def payment(request,id):
   booking = tbl_shopbooking.objects.get(id=id)
   scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
   amount = scrap.Scrap_Price
   if request.method == "POST":
      booking.shopbooking_status = 3
      booking.save()
      return redirect("Shop:loader")
   else:
      return render(request,"Shop/Payment.html", {"total":amount})

def loader(request):
    return render(request,"Shop/Loader.html")

def paymentsuc(request):
    return render(request,"Shop/Payment_suc.html")


def AddScrap(request):
   if "sid" in request.session:
      cat=tbl_category.objects.all()
      scrap = tbl_Scrap.objects.filter(Shop=request.session["sid"])
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
        Shop=tbl_newShop.objects.get(id=request.session["sid"])
      )
        return render(request,'Shop/AddScrap.html',{'msg':"Data Inserted"})
      else:
         return render(request,'Shop/AddScrap.html',{'category':cat,"scrap":scrap})
   else:
      return redirect("Guest:LoginForm")

def delscrap(request,id):
    tbl_Scrap.objects.get(id=id).delete()
    return render(request,'Shop/AddScrap.html',{'msg':"Data Deleted"})

def collectscarp(request, id):
   scarp = tbl_shopbooking.objects.get(id=id)
   scarp.shopbooking_status = 4
   scarp.save()
   s = tbl_Scrap.objects.get(id=scarp.scarp.id)
   s.scarp_status = 2
   s.save()
   return render(request,"Shop/View_Booking.html",{"msg":"Scarp Collected"})

def companybooking(request):
   if "sid" in request.session:
      scrap = tbl_companybooking.objects.filter(scarp__Shop=request.session["sid"])
      return render(request,"Shop/CompanyBooking.html",{"book":scrap})
   else:
      return redirect("Guest:LoginForm")

def verifyrequest(request, id, status):
   booking= tbl_companybooking.objects.get(id=id)
   booking.companybooking_status = status
   booking.save()
   scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
   scrap.scarp_status=1
   scrap.save()
   msg =""
   if status == 1:
      msg = "Request Accepted"
   else:
      msg = "Request Rejected"
   return render(request,"Shop/CompanyBooking.html" ,{"msg":msg})