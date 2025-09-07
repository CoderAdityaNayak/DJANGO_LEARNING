from django.shortcuts import render
from .forms import NumberListForm               

def home(request):
    squared_list=[]
    if request.method=="POST":
        form=NumberListForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['numbers']
            try:
                num_list=[int(x.strip()) for x in data.split(",")] # convert to ints
                squared_list=[n*n for n in num_list]
                
            except ValueError:
             squared_list=["VALUE ERROR , WHAT MAN YOU =) "]

    else:
        form=NumberListForm()

    return render(request,"app4/index.html",{"form":form, "output":squared_list})
