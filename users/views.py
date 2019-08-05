from django.shortcuts import render, HttpResponse, redirect, render_to_response, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from .models import OrgProfile, UserProfile
from .forms import OrgSignUpForm, UserSignUpForm, OrgProfileUpdateForm, UserProfileUpdateForm
from core.models import VolLoc
# Create your views here.


def register(request):
    return redirect('/')

def registerOrg(request):

    registered = False
    if request.method == 'POST':
        form = OrgSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            messages.success(request, f"Account for {username} has been created!")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            registered = True
            return redirect('index')

    else:
        form = OrgSignUpForm()

    args = {'org_form':form}
    return render(request, 'users/registerOrg.html', args)

def registerUser(request):

    registered = False
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Account for {username} has been created!")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            registered = True
            return redirect('index')

    else:
        form = UserSignUpForm()

    args = {'user_form':form}
    return render(request, 'users/registerUser.html', args)


def orgLogout(request):
    logout(request)
    messages.success(request, f"Logged Out")
    return redirect('/')

@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.isUser==True:
            form = UserProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.userprofile)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

        else:
            form = OrgProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.orgprofile)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

    else:
        if request.user.isUser==True:
            form = UserProfileUpdateForm(instance=request.user.userprofile)
        else:
            form = OrgProfileUpdateForm(instance=request.user.orgprofile)

    if request.user.isUser is True:
        context = {
            'form': form,
            }
    else:
        context = {
            'form' : form,
            'locs' : VolLoc.objects.filter(creator=request.user),
            'nloc' : VolLoc.objects.filter(creator=request.user).count()
        }

    

    return render(request, 'users/profile.html', context)


    user = request.user

    loc = VolLoc.objects.filter(creator=request.user)
    return render(request, 'users/profile.html', {'user': user, 'loc': loc })

@login_required
def updateAccount(request):
    u_form=OrgUpdateForm()
    p_form = OrgProfileUpdateForm()

    args = {u_form:'u_form', p_form:'p_form'}

    return render(request, 'users/updateAccount.html', args)
