from django.shortcuts import render, redirect
from users_app.forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method=="POST":
        register_form =  CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Successfully Created Account. Login")
        return redirect('login', permanent=True)
            
    else:
        register_form =  CustomRegisterForm()
    return render(request, 'register.html' , {'register_form': register_form })


