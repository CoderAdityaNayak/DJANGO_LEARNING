from django.shortcuts import render
from .forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=getSqr(n1)  #get factorial for all numbers upto limit1
            return render(request,"app6/index.html",{'param1':result,'form':form1})
    else:
        form1=inputform() 
    return render(request,"app6/index.html",{'form':form1})

def square(n1):
    sqr1=n1*n1
    return sqr1

def getSqr(limit1):
    list1=[]
    list2=[]
    for i in range(1,limit1+1,1):
        list1.append(square(i))
        list2.append(i)
    return zip(list1,list2)