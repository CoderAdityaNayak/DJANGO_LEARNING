from django.shortcuts import render

def home(request):
    num1=5
    num2=4
    result=num1+num2
    return render(request,'app1/index.html',{'param1':result})
