from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *


# Create your views here.
def LoginForm(request):
    if request.method == "POST":
       email = request.POST.get("email")
       password = request.POST.get("password")

       usercount = tbl_user.objects.filter(User_Email=email,User_Password=password).count() 
       admincount=tbl_Registration.objects.filter(Registration_email=email,Registration_password=password).count()
       shopcount = tbl_newShop.objects.filter(Shop_Email=email, Shop_Password=password).count()
       companycount = tbl_company.objects.filter(Company_Email=email,Company_Password=password).count()
      
       if usercount > 0 :
        user = tbl_user.objects.get(User_Email=email, User_Password=password)
        request.session["uid"] = user.id
        return redirect("User:HomePage")
       elif admincount > 0 :
        admin = tbl_Registration.objects.get(Registration_email=email,Registration_password=password)
        request.session["aid"] = admin.id
        return redirect("Admin:HomePage")
       elif shopcount > 0:
        shop = tbl_newShop.objects.get(Shop_Email=email, Shop_Password=password)
        if shop.Shop_status == 0:
            return render(request, 'Guest/LoginForm.html', {"msg":"Your Verification is pending"})
        elif shop.Shop_status == 2:
            return render(request, 'Guest/LoginForm.html', {"msg":"Your Verification is rejected"})
        else:
            request.session["sid"] = shop.id
            return redirect("Shop:HomePage")
       elif companycount > 0:
        company = tbl_company.objects.get(Company_Email=email,Company_Password=password)
        if company.Company_status == 0:
            return render(request, 'Guest/LoginForm.html', {"msg":"Your Verification is pending"})
        elif company.Company_status == 2:
            return render(request, 'Guest/LoginForm.html', {"msg":"Your Verification is rejected"})
        else:
            request.session["cid"] = company.id
            return redirect("Company:HomePage")
       else: 
        return render(request, 'Guest/LoginForm.html', {"msg":"invalid Data"})
    else:
        return render(request,'Guest/LoginForm.html')


def SignUpForm(request):
    dis=tbl_district.objects.all()
    place=tbl_Place.objects.all()
    if request.method == "POST":
            place=tbl_Place.objects.get(id=request.POST.get("selplace"))
            Name=request.POST.get('name')
            Address=request.POST.get('txtaddress')
            Contact=request.POST.get('contact')
            Email=request.POST.get('email')
            Gender=request.POST.get('gender')
            Dob=request.POST.get('dob')
            Password=request.POST.get('password')
            Photo=request.FILES.get('txtfile')
            tbl_User.objects.create(
            Place=place,
            User_Name=Name,
            User_Address=Address,
            User_Contact=Contact,
            User_Email=Email,
            User_Gender=Gender,
            User_Dob=Dob,
            User_Password=Password,
            User_Photo=request.FILES.get("txtfile")
            )
            return redirect('Guest:SignUpForm')
    else:
            return render(request,'Guest/SignUpForm.html',{'district':dis})

def Shop(request):
    dis=tbl_district.objects.all()
    Place=tbl_Place.objects.all()
    if request.method == "POST":
        Place=tbl_Place.objects.get(id=request.POST.get("selplace"))
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Contact=request.POST.get('contact')
        Address=request.POST.get('txtaddress')
        Photo=request.FILES.get('txtphoto')
        Proof=request.FILES.get('txtproof')
        tbl_newShop.objects.create(
        Place=Place,        
        Shop_Name=Name,
        Shop_Email=Email,
        Shop_Contact=Contact,
        Shop_Address=Address,
        Shop_Photo=request.FILES.get("txtphoto"),
        Shop_Proof=request.FILES.get("txtproof"),
        Shop_Password=request.POST.get('password')
        )
        return render(request,'Guest/Shop.html')
    else:
        return render(request,'Guest/Shop.html',{'district':dis})

def company(request):
    dis=tbl_district.objects.all()
    place=tbl_Place.objects.all()
    if request.method == "POST":
            Name=request.POST.get('name')
            Email=request.POST.get('email')
            Contact=request.POST.get('contact')
            Address=request.POST.get('txtaddress')
            Photo=request.FILES.get('txtphoto')
            Proof=request.FILES.get('txtproof')
            tbl_company.objects.create(
            Place=tbl_Place.objects.get(id=request.POST.get("selplace")),        
            Company_Name=Name,
            Company_Email=Email,
            Company_Contact=Contact,
            Company_Address=Address,
            Company_Photo=request.FILES.get("txtphoto"),
            Company_Proof=request.FILES.get("txtproof"),
            Company_Password=request.POST.get("password")
            )
            return render(request,'Guest/Company.html')
    else:
            return render(request,'Guest/Company.html',{'district':dis})

def ajaxplace(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))   
    Place = tbl_Place.objects.filter(district=district)
    return render(request,"Guest/AjaxPlace.html",{"place":Place})

def index(request):
    return render(request,"Guest/index.html")