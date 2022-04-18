from django.shortcuts import render,redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#user -username = user password = test@123456
# Create your views here.
#We are checking here if user is anonymous/unknown/unauthenticated, then we will direct user to the login page or we will return render index page.
def index(request):
    #print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)

        #Authenticating users and login() was used
        user = authenticate(request,username=username, password=password)
        #“is not” – Returns true for any users except for user with value “None”
        if user is not None: 
            login(request,user)
            return redirect('/')
        # A backend authenticated the credentials
            
        else:
            return render(request,'login.html')
            
        # No backend authenticated the credentials

    return render(request,'login.html')

def logoutUser(request):
#Once user is logged out ,we will redirect user to the login page.    
    logout(request)
    return redirect('/login')  