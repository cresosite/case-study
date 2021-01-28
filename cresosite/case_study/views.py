from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from case_study.forms import SignUpForm, EditProfileForm, EditPasswordForm, ResponseForm
from case_study.models import Response
from django.contrib.auth.decorators import login_required


# Create your views here.

##################################### INDEX PAGE ###############################

def index(request):
    return render(request, 'case_study/index.html', {})

################################# INDEX PAGE ENDS ##############################

################################# USER LOGIN ###################################

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You are now logged In!"))
            return redirect('study_reponse')
            # return redirect('study')
        else:
            messages.success(request, ("Error in login! Please try again"))
            return redirect('login')
    else:
        return render(request, 'case_study/login.html', {})

######################### USER LOGIN ENDS ######################################


######################## USER LOGOUT ###########################################

def logout_user(request):
    logout(request)
    messages.success(request, ('You are now logged out!'))
    return redirect('index')

###################### USER LOGOUT ENDS ########################################


################### USER REGISTRATION ##########################################

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Sign Up Successful! Please proceed with the case study.'))
            return redirect('study_reponse')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'case_study/register.html', context)


################## USER REGITRATION ENDS #######################################


################## USERS-UPDATE FOR DETAILS ####################################

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have updated your profile!'))
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'case_study/edit_profile.html', context)


################ USERS-UPDATE FOR DETAILS ENDS #################################


############### USERS CHANGING THEIR PASSWORDS ##################################

def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user) # I changed PasswordChangeForm to EditPasswordForm because of my addition in forms.py
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have changed your password!'))
            return redirect('index')
    else:
        form = EditPasswordForm(user=request.user) # I changed PasswordChangeForm to EditPasswordForm because of my addition in forms.py

    context = {'form': form}
    return render(request, 'case_study/change_password.html', context)

################ USERS CHANGING THEIR PASSWORDS ENDS HERE ######################


#################### MY ADDED VIEWS ############################################


################### ABOUT ######################################################

def about(request):
    return render(request, 'case_study/about.html', {})

####################### ABOUT ENDS #############################################

@login_required
def study_reponse(request):
    try:
        profile = request.user.response
    except Response.DoesNotExist:
        profile = Response(user=request.user)
    if request.method == "POST":
        form = ResponseForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,("Thank you for completing the case study!"))
            return redirect('index')
    else:
        form = ResponseForm(instance=profile)
    context = {'form': form}
    return render(request, 'case_study/case_study_one.html', context)
