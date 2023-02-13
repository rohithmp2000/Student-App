from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def Register(request):
    if request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_name = request.POST.get('username')
        e_mail = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(firstname,lastname,password1)
        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                print("Username already exist !")
                messages.info(request,"Username already exist !")
                return redirect('register')
            elif User.objects.filter(email = e_mail).exists():
                print("Email already exist !")
                messages.info(request,"Email already exist !")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=user_name,email=e_mail,password=password1)
                user.save()
                print("Username Created !")
                messages.info(request,"Username Created !")
                return redirect('home')
        else:
            print("Password is not matching !")
            messages.info(request,"Password is not matching !")
            return redirect('register')
    return render(request,'Register.html')

def Login(request):
    print("Inside def")
    if request.method == 'POST':
        print("Inside if")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            print("Inside auth if")
            auth.login(request,user)
            return redirect('/student_home/')
        else:
            print("Inside auth else")
            messages.info(request,"User not found !")
            return render(request, 'Login.html')
    return render(request, 'Login.html')

def Logout(request):
    auth.logout(request)
    return render(request, 'Home.html')
