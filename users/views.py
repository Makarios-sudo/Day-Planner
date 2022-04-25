
from django.shortcuts import redirect, render

from .forms import RegisterNewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# Create your views here.

"""views for Registeration"""
def RegisterUser(request):
    form = RegisterNewUser()

    if request.method == 'POST':
        form = RegisterNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)
   


"""views for Login"""
def LoginUser(request):
    
    form = AuthenticationForm()
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
              
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, "Please Fill Out All the Fields")

    context = {'form': form}
    return render(request, 'registration/login.html', context)



"""views for logout"""
def LogOutUser(request):
    logout(request)
    return redirect('index')

