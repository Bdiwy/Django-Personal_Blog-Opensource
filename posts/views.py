from django.shortcuts import render
from .models import post
# Create your views here.
def index(request):
    context=post.objects.all()
    return render(request,'index.html',{'context':context})




def Blog(request,pk):
    context=post.objects.all()
    return render(request,'Blog.html',{'context':context ,'pk':pk})




def Services(request):
    return render(request,'Services.html')




def about(request):
    return render(request,'about.html')




def contact(request):
    return render(request,'contact.html')