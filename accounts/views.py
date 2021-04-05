from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from  module.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if (request.user.is_authenticated):
        if patient.objects.filter(email=request.user).exists():
            return redirect('/module/patient')
        elif doctor.objects.filter(email=request.user).exists():
            return redirect('/module/doctor')
        elif receptionist.objects.filter(email=request.user).exists():
            return redirect('/module/receptionist')
    else:
        return redirect('/login')

def login(request):
    if request.method == 'POST':
        type=request.POST['type']
        username = request.POST['email']
        passw = request.POST['password']
        user= auth.authenticate(username=username ,password=passw)
        
        if type =='patient' and user is not None:
            if patient.objects.filter(email=username).exists():
                auth.login(request,user)
                return redirect('/module/patient/')
            else:
                messages.info(request,'Patient Does Not Exist')
                return redirect('/login')
        elif type =='doctor' and user is not None:
            if doctor.objects.filter(email=username):
                auth.login(request,user)
                return redirect('/module/doctor')
            else:
                messages.info(request,'Doctor Does Not Exist')
                return redirect('/login')
        elif type=="receptionist" and user is not None :
            if receptionist.objects.filter(email=username):
                auth.login(request,user)
                return redirect('/module/receptionist')
            else:
                messages.info(request,'Receptionist Does Not Exist')
                return redirect('/login')
        else:
            print('else')
            messages.info(request,'invalid credentials') 
            return redirect('/login')

    else:
        print('django is chutiya')
        return render(request , 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_nam = request.POST['last_name']
        username = request.POST['email']
        password1 = request.POST['password']
        password = request.POST['password1']
        phn_no = request.POST['phn_no']
        gender = request.POST['gender']
        address = request.POST['address']
        
        #lol.append(username)
        if(password == password1):
            print("password match")
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'E-Mail Exists try different one..!!')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username , password=password,first_name=first_name , last_name=last_nam)
                patient(name= first_name+" "+last_nam, email=username,mobile=phn_no,gender=gender,address=address).save()
                user.save();
                return redirect('/module/patient') 
        else:
            messages.info(request,'password must match')
            return redirect('/register')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')