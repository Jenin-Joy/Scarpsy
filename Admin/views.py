from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def logout(request):
    del request.session["aid"]
    return redirect("Guest:LoginForm")

def District(request):
    if "aid" in request.session:
        dis=tbl_district.objects.all()
        if request.method=="POST":
            district_name=request.POST.get('txt_district')
            tbl_district.objects.create(
                district_name=district_name
            )
            # print(district_name)
            return render(request,'Admin/District.html',{'msg':"Data Inserted"})
        else:
            return render(request,'Admin/District.html',{'district':dis})
    else:
        return redirect("Guest:LoginForm")

def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return render(request,'Admin/District.html',{'msg':"Data Deleted"})


def editdistrict(request,id): 
    dis=tbl_district.objects.get(id=id)
    if request.method=="POST":
        district=request.POST.get('txt_district')
        dis.district_name=district
        dis.save()
        return render(request,'Admin/District.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/District.html',{'disdata':dis})  



def Category(request):
    if "aid" in request.session:
        cat=tbl_category.objects.all()
        if request.method=="POST":
            category_name=request.POST.get('txt_category')
            tbl_category.objects.create(
                category_name=category_name
            )

            return render(request,'Admin/Category.html',{'msg':"Data Inserted"})
        else:
            return render(request,'Admin/Category.html',{'category':cat})
    else:
        return redirect("Guest:LoginForm")

def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return render(request,'Admin/Category.html',{'msg':"Data Deleted"})


def editcategory(request,id): 
    cat=tbl_category.objects.get(id=id)
    if request.method=="POST":
        category=request.POST.get('txt_category')
        cat.category_name=category
        cat.save()
        return render(request,'Admin/Category.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Category.html',{'catdata':cat})  

def Registration(request):
    if "aid" in request.session:
        reg=tbl_Registration.objects.all()
        if request.method=="POST":
            Admin_name=request.POST.get('name')
            Admin_email=request.POST.get('email')
            Admin_password=request.POST.get('password')
            tbl_Registration.objects.create(
            Registration_name=Admin_name,
            Registration_email=Admin_email,
            Registration_password=Admin_password,
            )
            return render(request,'Admin/Registration.html',{'msg':"Registred Sucessfully"})
        else:
            return render(request,'Admin/Registration.html',{'Registration':reg})
    else:
        return redirect("Guest:LoginForm")


def delRegistration(request,id):
    tbl_Registration.objects.get(id=id).delete()
    return render(request,'Admin/Registration.html',{'msg':"Data Deleted"})

def editRegistration(request,id): 
    reg=tbl_Registration.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        reg.Registration_name=name
        reg.Registration_email=email
        reg.Registration_password=password
        reg.save()
        return render(request,'Admin/Registration.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Registration.html',{'regdata':reg})  

    
def Place(request):
    if "aid" in request.session:
        dis=tbl_district.objects.all()
        place=tbl_Place.objects.all()
        if request.method=="POST":
            tbl_Place.objects.create(
                district=tbl_district.objects.get(id=request.POST.get('seldistrict')),
                Place_name=request.POST.get("txt_place")
            )
            return render(request,'Admin/Place.html',{'msg':"Data Inserted"})
        else:
            return render(request,'Admin/Place.html',{'district':dis,'place':place})
    else:
        return redirect("Guest:LoginForm")


def delPlace(request,id):
    tbl_Place.objects.get(id=id).delete()
    return render(request,'Admin/Place.html',{'msg':"Data Deleted"})

def editPlace(request,id): 
    dis=tbl_district.objects.all()
    pal=tbl_Place.objects.get(id=id)
    if request.method=="POST":
        pal.district=tbl_district.objects.get(id=request.POST.get('seldistrict'))
        pal.Place_name=request.POST.get("txt_place")
        pal.save()
        return render(request,'Admin/Place.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Place.html',{'editplacedata':pal,'district':dis})  


def HomePage(request):
    if "aid" in request.session:
        return render(request,'Admin/HomePage.html')
    else:
        return redirect("Guest:LoginForm")


def newshop(request):
    if "aid" in request.session:
        shop=tbl_newShop.objects.filter(Shop_status=0)
        return render(request,'Admin/NewShop.html',{'shop':shop})
    else:
        return redirect("Guest:LoginForm")

def verifyshop(request,id,status):
    shop = tbl_newShop.objects.get(id=id)
    shop.Shop_status=status
    shop.save()
    msg = ""
    if status == 1:
        msg = "Shop Approved"
    else:
        msg = "Shop Rejected"
    return render(request,"Admin/HomePage.html",{"msg":msg})

def approvedshop(request):
    if "aid" in request.session:
        shop=tbl_newShop.objects.filter(Shop_status=1)
        return render(request,'Admin/Approved_shop.html',{'shop':shop})
    else:
        return redirect("Guest:LoginForm")

def rejectedshop(request):
    if "aid" in request.session:
        shop=tbl_newShop.objects.filter(Shop_status=2)
        return render(request,'Admin/Rejected_shop.html',{'shop':shop})
    else:
        return redirect("Guest:LoginForm")

def subcategory(request):
    if "aid" in request.session:
        category=tbl_category.objects.all()
        subcategory=tbl_subcategory.objects.all()
        if request.method=="POST":
            tbl_subcategory.objects.create(
                category=tbl_category.objects.get(id=request.POST.get('selcategory')),
                subcategory_name=request.POST.get("txt_Subcategory")
            )
            return render(request,'Admin/SubCategory.html',{'msg':"Data Inserted"})
        else:
            return render(request,'Admin/SubCategory.html',{'category':category,'subcategory':subcategory})
    else:
        return redirect("Guest:LoginForm")


def delsubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return render(request,'Admin/SubCategory.html',{'msg':"Data Deleted"})

def editsubcategory(request,id): 
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        subcategory.category=tbl_category.objects.get(id=request.POST.get('selcategory'))
        subcategory.subcategory_name=request.POST.get("txt_Subcategory")
        subcategory.save()
        return render(request,'Admin/SubCategory.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/SubCategory.html',{'editsubcategory':subcategory,'category':category})

def newcompany(request):
    if "aid" in request.session:
        company=tbl_company.objects.filter(Company_status=0)
        return render(request,'Admin/New_Company.html',{'company':company})
    else:
        return redirect("Guest:LoginForm")

def verifycompany(request,id,status):
    Company = tbl_company.objects.get(id=id)
    Company.Company_status=status
    Company.save()
    msg = ""
    if status == 1:
        msg = "Company Approved"
    else:
        msg = "Company Rejected"
    return render(request,"Admin/HomePage.html",{"msg":msg})

def approvedcompany(request):
    if "aid" in request.session:
        company=tbl_company.objects.filter(Company_status=1)
        return render(request,'Admin/Approved_company.html',{'company':company})
    else:
        return redirect("Guest:LoginForm")

def rejectedcompany(request):
    if "aid" in request.session:
        company=tbl_company.objects.filter(Company_status=2)
        return render(request,'Admin/Rejected_company.html',{'company':company})
    else:
        return redirect("Guest:LoginForm")

def viewcomplaint(request):
    if "aid" in request.session:
        user = tbl_user.objects.all()
        company = tbl_company.objects.all()
        shop = tbl_newShop.objects.all()
        userdata = tbl_Complaint.objects.filter(User__in=user,Complaint_Status=0)
        shopdata = tbl_Complaint.objects.filter(Shop__in=shop,Complaint_Status=0)
        companydata = tbl_Complaint.objects.filter(Company__in=company,Complaint_Status=0)
        return render(request,"Admin/ViewComplaints.html",{'company':companydata,"shop":shopdata,"user":userdata})
    else:
        return redirect("Guest:LoginForm")

def reply(request, id):
    if request.method == "POST":
        complaint = tbl_Complaint.objects.get(id=id)
        complaint.Complaint_Status = 1
        complaint.Complaint_Replay = request.POST.get("txt_reply")
        complaint.save()
        return render(request, "Admin/Reply.html", {"msg": "Reply sent successfully"})
    else:
        return render(request, "Admin/Reply.html")

def replyedcomplaint(request):
    if "aid" in request.session:
        user = tbl_user.objects.all()
        company = tbl_company.objects.all()
        shop = tbl_newShop.objects.all()
        userdata = tbl_Complaint.objects.filter(User__in=user,Complaint_Status=1)
        shopdata = tbl_Complaint.objects.filter(Shop__in=shop,Complaint_Status=1)
        companydata = tbl_Complaint.objects.filter(Company__in=company,Complaint_Status=1)
        return render(request,"Admin/ReplyedComplaint.html",{'company':companydata,"shop":shopdata,"user":userdata})
    else:
        return redirect("Guest:LoginForm")