from django.shortcuts import render

def home(request):
    numbers = [1, 2, 3, 4, 5,7,8,9,10]   # hardcoded
    squares = [n**2 for n in numbers]
    result = zip(numbers, squares)   # gives (n, sq)
    return render(request, "app7/index.html", {"param1": result})
