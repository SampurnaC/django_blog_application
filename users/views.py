from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login')
    else:
        form=UserRegisterForm()    
    context={'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method=="POST":
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()        
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(request.FILES, instance=request.user)    
    context = {'user_form': user_form,
               'profile_form': profile_form}
    return render(request, 'users/profile.html', context)
