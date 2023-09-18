from django.shortcuts import render,redirect, get_object_or_404, HttpResponse

from .models import Form,Branch
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login




# Create your views here.
def index(request):
    return render(request,'Home.html')



def register(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        cpassword = request.POST.get('psw-repeat')
        if User.objects.filter(username=username).exists():
            return HttpResponse("This username is already taken. Please choose a different one.")
        if password != cpassword:
            return HttpResponse("Your Password and Confirm Password are not matching !!")
        else:
            my_user = User.objects.create_user(username=username,password=password)
            my_user.set_password(password)
            my_user.save()
            return redirect('login')
    return render(request, 'register.html')

def loginn(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('form_page')
        else:
            return HttpResponse("Invalid Login Credentials!!!")
    return render(request,'login.html')



def appform(request):
    reg_form=RegistrationForm()
    context = {
        'form':reg_form
        }
    return render(request,'form.html',context)

def save_appform(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'submit.html')
    else:
        form = RegistrationForm()
    return render(request,'form.html',{'form':form} )


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request,'branches_dropdown_list_options.html', {'branches': branches})








