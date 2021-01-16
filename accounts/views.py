from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        # checking password match
        if  password !=password2:
            messages.error(request,  "Passwords do not match!")
            return redirect('register')

        # Check if username exists in db or not
        if User.objects.filter(username=username).exists():
            messages.error(request,  "Username already taken!")
            return redirect('register')

        # Check if email exists in db or not
        if User.objects.filter(email=email).exists():
            messages.error(request,  "Email already registered!")
            return redirect('register')

        # All test passed
        user= User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name, password=password)

        # auth.login(request,user)
        #messages.success(request, "You are now logged in.")
        messages.success(request, "You are now logged in.")
        user.save()
        messages.success(request, "You are now registered and can login.")
        return redirect('login')
    else:
        return render(request,'accounts/register.html')

# Login user
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # If user doesnot exist
        if not user:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        # USer authentication successfull
        auth.login(request,user)
        messages.success(request,  'You are now logged in.')
        return redirect('dashboard')

    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        messages.success(request,'Successfully Logged Out!')
        return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')