from django.http import HttpResponse
from django.shortcuts import render
from . models import place


# Create your views here.
def demo(request):
   obj=place.objects.all()

   return render(request,'index.html',{'result':obj})
# def addition(request):res
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,"result.html",{'result':res})