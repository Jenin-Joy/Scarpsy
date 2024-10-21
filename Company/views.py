from django.shortcuts import render,redirect
from Admin.models import *
from Company.models import *
from Guest.models import *
from User.models import *
from django.db.models import Sum
from django.http import JsonResponse
# Create your views here.

def HomePage(request):
    if "cid" in request.session:
        return render(request,'Company/HomePage.html')
    else:
        return redirect("Guest:LoginForm")

def logout(request):
    del request.session["cid"]
    return redirect("Guest:LoginForm")


def Profile(request):
    if "cid" in request.session:
        company=tbl_company.objects.get(id=request.session['cid'])
        return render(request,'Company/Profile.html',{'company':company})
    else:
        return redirect("Guest:LoginForm")


def EditProfile(request):
    if "cid" in request.session:
        company=tbl_company.objects.get(id=request.session['cid'])
        if request.method == "POST":
            company.Company_Name = request.POST.get("name")
            company.Company_Address = request.POST.get("address")
            company.Company_Contact = request.POST.get("contact")
            company.company_Email = request.POST.get("email")
            company.save()
            return render(request,'Company/EditProfile.html',{'msg':"Profile Updated"})
        else:
            return render(request,'Company/EditProfile.html',{'company':company})
    else:
        return redirect("Guest:LoginForm")


def ChangePassword(request):
    if "cid" in request.session:
        company=tbl_company.objects.get(id=request.session['cid'])
        if request.method == "POST":
            if company.Company_Password == request.POST.get("old"):
                if request.POST.get("new") == request.POST.get("retype"):
                    company.Company_Password = request.POST.get("retype")
                    company.save()
                    return render(request,'Company/ChangePassword.html',{"msg":"Profile Updated"})
                else:
                    return render(request,'Company/ChangePassword.html',{"msg1":"Error In Re Password"})
            else:
                return render(request,'Company/ChangePassword.html',{"msg1":"Error In Old Password"})
        else:
            return render(request,'Company/ChangePassword.html')
    else:
        return redirect("Guest:LoginForm")


def Complaint(request):
    if "cid" in request.session:
        complaint = tbl_Complaint.objects.filter(Company=request.session["cid"])
        if request.method=="POST":
            Title=request.POST.get('txttitle')
            Content=request.POST.get('txtcontent')
            Company=tbl_company.objects.get(id=request.session["cid"])
            tbl_Complaint.objects.create(       
            Complaint_Title=Title,
            Complaint_Content=Content,
            Company=Company
        )
            return redirect("Company:Complaint")
        else:
            return render(request,'Company/Complaint.html',{"complaint":complaint})
    else:
        return redirect("Guest:LoginForm")


def FeedBack(request):
    if "cid" in request.session:
        if request.method=="POST":
            Content=request.POST.get('txtcontent')
            tbl_FeedBack.objects.create(       
                Feedback_Content=Content,
            )
            return redirect("Company:FeedBack")
        else:
            return render(request,'Company/FeedBack.html')
    else:
        return redirect("Guest:LoginForm")

def ViewScrap(request):
    if "cid" in request.session:
        shop = tbl_newShop.objects.all()
        scrap = tbl_Scrap.objects.filter(scarp_status=0,Shop__in=shop)
        return render(request,'Company/ViewScrap.html',{'scrap':scrap})
    else:
        return redirect("Guest:LoginForm")
      
def sendrequest(request, id):
   tbl_companybooking.objects.create(company=tbl_company.objects.get(id=request.session["cid"]),scarp=tbl_Scrap.objects.get(id=id))
   return render(request,"Company/ViewScrap.html",{"msg":"Request Sended"})


def Booking(request):
    if "cid" in request.session:
        booking = tbl_companybooking.objects.filter(company=request.session["cid"])
        return render(request,"Company/Booking.html",{"booking":booking})
    else:
        return redirect("Guest:LoginForm")

def payment(request,id):
   booking = tbl_companybooking.objects.get(id=id)
   scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
   amount = scrap.Scrap_Price
   if request.method == "POST":
      booking.companybooking_status = 3
      booking.save()
      return redirect("Company:loader")
   else:
      return render(request,"Company/Payment.html", {"total":amount})

def loader(request):
    return render(request,"Company/Loader.html")

def paymentsuc(request):
    return render(request,"Company/Payment_suc.html")

def collectscarp(request, id):
   scarp = tbl_companybooking.objects.get(id=id)
   scarp.companybooking_status = 4
   scarp.save()
   s = tbl_Scrap.objects.get(id=scarp.scarp.id)
   s.scarp_status = 2
   s.save()
   return render(request,"Company/Booking.html",{"msg":"Scarp Collected"})

def addproduct(request):
    if "cid" in request.session:
        product = tbl_product.objects.filter(company=request.session["cid"])
        if request.method == "POST":
            tbl_product.objects.create(product_name=request.POST.get("txt_name"),
                                        product_price=request.POST.get("txt_price"),
                                        product_photo=request.FILES.get("txt_photo"),
                                        company=tbl_company.objects.get(id=request.session["cid"]))
            return render(request, "Company/AddProduct.html", {"msg":"Produt Added"})
        else:
            return render(request, "Company/AddProduct.html",{"product": product})
    else:
        return redirect("Guest:LoginForm")

def deleteproduct(request, id):
    tbl_product.objects.get(id=id).delete()
    return render(request,"Company/AddProduct.html", {"msg": "Product Deleted"})

def addstock(request, id):
    stock = tbl_stock.objects.filter(product=id)
    if request.method == "POST":
        tbl_stock.objects.create(stock=request.POST.get('txt_stock'), product=tbl_product.objects.get(id=id))
        return render(request,"Company/AddStock.html",{"msg":"Stock Added successfully", "id":id})
    else:
        return render(request,"Company/AddStock.html",{"stock":stock,"id":id})

def deletestock(request, id, pid):
    tbl_stock.objects.get(id=id).delete()
    return render(request,"Company/AddStock.html", {"msg": "Stock Deleted", "id":pid})

def viewproduct(request):
    if "cid" in request.session:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        product = tbl_product.objects.exclude(company__id=request.session["cid"])
        for i in product:
            total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock'))['total']
            total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
            # print(total_stock)
            # print(total_cart)
            if total_stock is None:
                total_stock = 0
            if total_cart is None:
                total_cart = 0
            total =  total_stock - total_cart
            i.total_stock = total

            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(product,parry)
        return render(request,"Company/ViewProduct.html",{"product":datas,"ar":ar})
    else:
        return redirect("Guest:LoginForm")

def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    Companydata=tbl_company.objects.get(id=request.session["cid"])
    bookingcount=tbl_booking.objects.filter(company=Companydata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(company=Companydata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"Company/ViewProduct.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"Company/ViewProduct.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(company=Companydata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"Company/ViewProduct.html",{'msg':msg})

def Mycart(request):
    if "cid" in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("Company:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(company=request.session["cid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(company=request.session["cid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock'))['total']
                    total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"Company/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"Company/MyCart.html")
    else:
        return redirect("Guest:LoginForm")
        

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("Company:Mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("Company:Mycart")   

def productpayment(request):
    if "cid" in request.session:
        bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
        amt = bookingdata.booking_amount
        if request.method == "POST":
            bookingdata.booking_status = 2
            bookingdata.save()
            return redirect("Company:loader")
        else:
            return render(request,"Company/Payment.html",{"total":amt})
    else:
        return redirect("Guest:LoginForm")

def mybooking(request):
    if "cid" in request.session:
        book = tbl_booking.objects.filter(company=request.session["cid"])
        return render(request,"Company/MyBooking.html",{"book":book})
    else:
        return redirect("Guest:LoginForm")

def reproductpayment(request, id):
    bookingdata = tbl_booking.objects.get(id=id)
    amt = bookingdata.booking_amount
    if request.method == "POST":
        bookingdata.booking_status = 2
        bookingdata.save()
        return redirect("Company:loader")
    else:
        return render(request,"Company/Payment.html",{"total":amt})

def myproducts(request, id):
    cart = tbl_cart.objects.filter(booking=id)
    return render(request, "Company/Myproducts.html", {"cart":cart})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"Company/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"Company/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-datetime')
    return render(request,"Company/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)