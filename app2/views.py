from django.shortcuts import render
from app2.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            num1=data.get("input1",1)
            num2=data.get("input2",1)
            result=num1+num2
            return render(request,"app2/index.html",{'param1':result})
    else:
        form1=inputform()
    return render(request,"app2/index.html",{'form':form1})


