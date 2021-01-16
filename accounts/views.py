from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        print('Submitted Form')
        messages.error(request, "Testing error messages")
        return redirect('login')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        print("Logged in requested")
        return redirect('index')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')