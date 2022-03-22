from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("Account created successfully", username)
            messages.success(request, f"Account created for username {username}!!!")
            return redirect('login')


    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_from = UserUpdateForm(request.POST, instance=request.user) # instances to get the current info of login user
        profile_form = ProfileUpdateForm(request.POST, request.FILES, ## request.files bc of image
                                        instance=request.user.profile)

        if user_from.is_valid() and profile_form.is_valid():
            user_from.save()
            profile_form.save()
            messages.success(request, f'Details has been updated!!!')
            return redirect('profile')
    else:
        user_from = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_from,
        'profile_form': profile_form
    }

    return render(request, 'accounts/profile.html', context)

