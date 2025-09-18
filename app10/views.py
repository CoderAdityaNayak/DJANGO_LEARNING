from django.shortcuts import render

def home(request):
    return render(request,'app10/index.html',{'param1':"hello"})
