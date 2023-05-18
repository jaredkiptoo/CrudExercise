from django.shortcuts import render

# Create your views here.
def website(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def bedroom(request):
    return render(request,'Bedroom.html')

def kitchen(request):
    return render(request, 'kitchen.html')

def dining(request):
    return render(request,'dining.html')

def backyard(request):
    return render(request,'backyard.html')
