from django.shortcuts import render

def index(request):
    return render(request,'blog/index.html')

def posts(request):
    return render(request,'') 

def singlepost(request):
    return render(request,'')       
