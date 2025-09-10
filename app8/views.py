from django.shortcuts import render
import datetime as dt
from app8.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            name=data1.get("name","kishan")
            p=data1.get("p",1)
            t=data1.get("t",1)
            r=data1.get("r",1)
            list1=calc1(p,t,r)
            si=list1[0]
            amount=list1[1]
            today=dt.datetime.now()
            maturity_date=calcdate(today)
            return render(request,"app8/index.html",{"param1":si,"param2":amount, "param3":p ,"param4":str(maturity_date),"name":name})
    else:
        form1=inputform()
    return render(request,"app8/index.html",{"form":form1})

def calc1(p,t,r):
    si=(p*t*r)/100
    amount=p+si
    return [si,amount,p]

def calcdate(today):
    return today+dt.timedelta(days=3*365)
