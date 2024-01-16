from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileAddMoneyForm
from django.contrib.auth import logout as logouts 
from django.contrib.auth.decorators import login_required
from .models import Profile
from .decorators import check_role
from django.db.models import F

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
@check_role
def profile(request):
    profile_instance, created = Profile.objects.get_or_create(user=request.user) # creating for allauth users so that they have profile instance
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileAddMoneyForm(request.POST,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            profile_instance.wallet_balance = F('wallet_balance') + p_form.cleaned_data['wallet_balance']
            profile_instance.save()
            profile_instance = Profile.objects.get(user=request.user)
            p_form = ProfileAddMoneyForm(instance=profile_instance, initial={'wallet_balance': 0})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileAddMoneyForm(initial={'wallet_balance': 0})
    context = {'u_form':u_form,'p_form':p_form,'wallet_balance': profile_instance.wallet_balance}
    return render(request,'users/profile.html',context)


def logout(request):
    logouts(request)
    if request.method == 'POST':
        return redirect('/logout/') 
    else:
        return redirect("myapp-home")
