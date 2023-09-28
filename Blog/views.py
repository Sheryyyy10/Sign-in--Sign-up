from django.shortcuts import render

# Create your views here.
def indexx(request):
    return render(request,"indexx.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def guards(request):
    return render(request,"guard.html")

