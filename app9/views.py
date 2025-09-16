from django.shortcuts import render
from .forms import toolkit 

def home(request):
    combined = []  #empty list for our values

    if request.method == "POST":
        form1 = toolkit(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            num1 = data.get("num1")
            num2 = data.get("num2")      

            num=[]
            sqr=[]
            cubes=[]
            for i in range(num1, num2+1,1):
                num.append(i)
                sqr.append(i*i)
                cubes.append(i*i*i)

            combined = zip(num, sqr, cubes)
    else:
        form1 = toolkit()  # empty form for GET requests

    return render(request, 'app9/index.html', {'form': form1, 'data': combined})
