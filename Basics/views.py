from django.shortcuts import render

# Create your views here.

def Sum(request):
    result=''
    if request.method=="POST":
        number1=int(request.POST.get('txtnum1'))
        number2=int(request.POST.get('txtnum2'))
        result=number1 + number2
    return render(request,'Basics/Sum.html',{'result':result})

def Sum3(request):
    result=''
    if request.method=="POST":
        number1=int(request.POST.get('txtnum1'))
        number2=int(request.POST.get('txtnum2'))
        number3=int(request.POST.get('txtnum3'))
        result=number1 + number2 + number3
    return render(request,'Basics/Sum3.html',{'result':result})


def calculator(request):
    result=''
    if request.method=="POST":
        number1=int(request.POST.get('txt_num1'))
        number2=int(request.POST.get('txt_num2'))
        btn=request.POST.get("btn_calc")
        if btn=='+':
            result=number1 + number2
        elif btn=='-' :
            result=number1 - number2
        elif btn=='*':
            result=number1 * number2
        elif btn=='/':
            result=number1 / number2

    return render(request,'Basics/Calculator.html',{'result':result})

def Largest(request):
    if request.method=="POST":
        number1 =int(request.POST.get('txtnum1'))
        number2 =int(request.POST.get('txtnum2'))
        if  number1 > number2 :
            result=number1
        else:
            result=number2    
        return render(request,'Basics/Largest.html',{'result':result})
    else:
            return render(request,'Basics/Largest.html')



def RankList(request):
    if request.method=="POST":
        FirstName=request.POST.get('fname')
        LastName=request.POST.get('lname')
        Gender=request.POST.get('gender')
        Department=request.POST.get('dept')
        Mark1=int(request.POST.get('m1'))
        Mark2=int(request.POST.get('m2'))
        Mark3=int(request.POST.get('m3'))
        if Gender== 'Male' :
            name='Mr. ' + FirstName +" " +LastName
        elif Gender=='Female' :
            name='Mrs. '+ FirstName + " "+LastName
        Total=Mark1 + Mark2 + Mark3   
        Percentage=Total / 300 * 100
        if Percentage >= 92:
            grade="A+"
        elif Percentage > 80: 
            grade="A"
        elif Percentage > 70:
            grade="B+"  
        elif Percentage > 60:
            grade="B"
        elif Percentage > 50:
            grade="c+"   
        elif Percentage > 40:
            grade="c" 
        elif Percentage >  30:
            grade="D+"  
        elif Percentage >  20:
            grade="D" 
        return render(request,'Basics/RankList.html',{'name':name,'gender':Gender,'dept':Department,'total':Total,'percentage':Percentage,'grade':grade})
    else:
        return render(request,'Basics/RankList.html')

