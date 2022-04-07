from django.shortcuts import render, redirect
from .form import Emp

# Create your views here.

def index(request):
    if request.method == "POST":
        a =Emp(request.POST)
        if a.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        a = Emp()
    return render(request,'index.html',{'form':a})