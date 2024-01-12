from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileAddMoneyForm
from django.contrib.auth import logout as logouts 
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            Profile.objects.create(user=form.instance)
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user) # creating for allauth users so that they have profile instance
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileAddMoneyForm(request.POST,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form= ProfileAddMoneyForm(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)


def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('/')
    else:
        return redirect(request,"myapp-home")
