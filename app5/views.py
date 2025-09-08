from django.shortcuts import render
from .forms import NumberListForm

def home(request):
    squared_list=[]
    if request.method=="POST":
        form=NumberListForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['numbers']
            try:
                num_list=[int(x.strip()) for x in data.split(",")]
                squared_list=[n*n for n in num_list]
            
            except ValueError:
                squared_list=["SOMETHING IS WRONG"]
    else:
        form=NumberListForm()
    
    
    return render(request,"app5/index.html",{"form":form,"output":squared_list})