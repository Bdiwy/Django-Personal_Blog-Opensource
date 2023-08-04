from django.shortcuts import render, redirect
from .models import post
from .models import Contact
from django.contrib import messages

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
    if request.method == 'POST' :
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        if not name:
            messages.info(request,'there is no name to send')
            return redirect('contact')
        elif not email:
            messages.info(request,'there is no email to send')
            return redirect('contact')
        elif not message:
            messages.info(request,'there is no message to send')
            return redirect('contact')
        else:
            contact = Contact.objects.create(name=name, email=email , message=message)
            messages.info(request,'thanx for useing our service')
            return redirect('index')
    return render(request,'contact.html')