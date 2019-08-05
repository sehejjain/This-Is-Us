from django.shortcuts import render, HttpResponse, redirect
#from .models import  VolLoc
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import VolLocCreationForm
from django.contrib.auth.decorators import permission_required

from users.models import User
from django.contrib import messages
from users.models import OrgProfile, UserProfile
from users.forms import OrgSignUpForm, UserSignUpForm, OrgProfileUpdateForm, UserProfileUpdateForm, LoginForm
from .models import VolLoc
# Create your views here.
def index(request):
    
    uform = UserSignUpForm()
    pform = OrgSignUpForm()
    form = LoginForm()
    args = {'user':request.user, 'user_form':uform, 'org_form':pform, 'form': form}
    return render(request, 'core/index.html', args)

def create_volloc(request):
    if request.method == 'POST':
        form =  VolLocCreationForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            loc = form.save(commit=False)
            loc.creator = request.user
            loc.save()
            print(form.errors.as_data())

            return redirect('/profile')
        if not form.is_valid():
            print('not')
    else:
        form = VolLocCreationForm()

    args = {'form':form}
    return render(request, 'core/createLoc.html', args)
