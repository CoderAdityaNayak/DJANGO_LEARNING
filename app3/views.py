from django.shortcuts import render
from app3.forms import inputform

def home(request):
    result = None  # Default value
    if request.method == "POST":
        form1 = inputform(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            num1 = data.get("time", 1)
            num2 = data.get("amount", 1)
            num3 = data.get("rate",1)
            result= ((num1*num2*num3)/100)
    else:
        form1 = inputform()

    return render(request, "app3/index.html", {
        'form': form1,
        'param1': result
    })
