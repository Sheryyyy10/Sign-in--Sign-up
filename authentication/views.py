from Tools.scripts import generate_token
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from GFG import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
# from .tokens import generate_token
from email.message import EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import uuid
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm
# Create your views here
def home(request):
    return render(request, "index.html")

def signup(request, email_subject=None,):
    form = Contactforms()
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some another username")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('signup')

        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name= lname
        myuser.is_active= False

        get_user_model()

        # Welcome Email

        subject = "Welcome to GFG-django login!!"
        message = "Hello" + myuser.first_name + "!! \n" + ("Welcome to GFG!! \n Thank you for visiting our website \n "
                                                           "\n\n Thanking You \n Shehryar")
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        uid = urlsafe_base64_encode(force_bytes(myuser.pk))
        print(uid)
        token = uuid
        # token = generate_token.make_token(myuser)
        print(token)
        return redirect(to='signin')
       #
       #  # Confirmation Email
       #  current_site = get_current_site(request)
       #  email_subject = "Confirm your email @ GFG-django login!!"
       #  message2 = render_to_string('email_confirmation.html',{
       #     'name': myuser.first_name,
       #     'domain': current_site.domain,
       #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
       #     'token': generate_token.make_token(myuser)
       #  })
       #  email = EmailMessage(
       #     email_subject,
       #     message2,
       #     settings.EMAIL_HOST_USER,
       #     [myuser.email],
       # )
       #  email.fail_silently = True
       #  email.send()

    return render(request, "signup.html", context={"signup_form":form})
def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credientals!")
            return redirect('home')


    return render(request, "signin.html")
def signout(request):
   logout(request)
   messages.success(request,"Log Out Successfully!")
   return redirect('home')


def force_text(param):
    pass


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

        if myuser is not None and generate_token.check_token(myuser,token):
            myuser.is_active = True
            myuser.save()
            login(request,myuser)
            return redirect('home')

        else:
            return redirect(request,'activation_failed.html')


def image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'image.html', {'form': form})
