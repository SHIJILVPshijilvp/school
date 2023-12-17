from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from schoolapp.models import Departments, Profiles


def home(request):
    return render(request, 'index.html')


def add(request):
    profiles = Profiles.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        phone = request.POST.get('phone', '')
        course = request.POST.get('course', '')
        gender = request.POST.get('gender', '')
        mail_id = request.POST.get('mail_id', '')
        DOB = request.POST.get('DOB', '')
        address = request.POST.get('address', '')
        department = request.POST.get('department', '')

        profile = Profiles(name=name, mail_id=mail_id, DOB=DOB, age=age, phone=phone, course=course, gender=gender,
                           address=address, department=department)
        profile.save()
    return render(request, 'submit.html', {'profiles': profiles})


def newpage(request):
    return render(request, 'new.html')


def profile(request):
    profile = Profiles.objects.all
    return render(request, 'profile.html', {'profile': profile})


def formpage(request):
    return render(request, 'form.html')


def submit(request):
    return render(request, 'submit.html')


# ,
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        # email = request.POST['email']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('schoolapp:register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'email taken')
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                print("user registered")
                return redirect('schoolapp:login')
        else:
            messages.info(request, 'password not matching')
            return redirect('schoolapp:register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('schoolapp:newpage')
        else:
            messages.info(request, 'invalid')
            return redirect('schoolapp:login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('schoolapp:home')
