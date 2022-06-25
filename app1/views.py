import re
from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'name':'dileep'}
    return render(request,'hai.html',context=d)
    

def hello(request):
    d={'a':30,'b':8}
    return render(request,'hai.html',context=d)

def dillu(request):
    d={'a':32, 'b':49, 'c':9}
    return render(request,'hai.html',d)    

def ravan(request):
    d={'a':32, 'b':49, 'c':9}
    return render(request,'hai.html',d)    

def khan(request):
    d={'name':'yaswanth'}
    return render(request,'looping.html',context=d)


