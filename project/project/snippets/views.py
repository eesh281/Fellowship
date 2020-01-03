import datetime
import json
import django
import jwt
from django.template.loader import render_to_string
from validate_email import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.conf import setting
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from rest_framework.views import APIView
from project.settings import EMAIL_HOST_USER,file_handler
from django.core.mail import send_mail
from snippets.token import token_activation,token_validation,account_activation_token
from rest_framework.response import Response
from .serializers import EmailSerializer,LoginSerializer, RegistrationSerializer, UserSerializer
#from django.core.validators import validate_email
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect , response
from jwt import ExpiredSignatureError
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

def home(request):
   
    return render(request, 'login.html')

class Login(GenericAPIView):

    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse("Your account was active.")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed, Not the Registered username or password")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")



class Registrations(GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        return render(request, 'registration.html')
        
    def post(self, request, *args, **kwargs):        
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        smd = {
            'success': False,
            'message': "not registered yet",
            'data': [],
        }

        if username == "" or name == "" or email == "" or password1 == "" or password2 == "":
            messages.warning(request, "Fields cannot be empty")
        elif password1 != password2:
            messages.warning(request, "password fields not matching")

        try:
            validate_email(email)
        except validate_email.ValidationError:
            messages.error(request, "Email id not valid")
            smd["success"] = False
            smd["message"] = "email"
            return HttpResponse(json.dumps(smd), status=400)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email id already registered")
            smd["success"] = False
            smd["message"] = "email exists occured"
            return HttpResponse(json.dumps(smd), status=400)

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already taken")

        try:
            user_created = User.objects.create_user(username=username, email=email, 
                                                    password=password1,
                                                    is_active=False)
            
            user_created.save()
            # send_mail(subject, message, from_mail, to_list, fail_silently=True)
            sub = 'Thank you for registering with fundoo notes'
            msg = 'U can do lot many things with fundoo like create notes, set remainders and ../n Have FunDooing'
            from_mail = "kour.gursheesh281@gmail.com"
            to_list = [user_created.email]
            send_mail(sub, msg, from_mail, to_list, fail_silently=True)
            print('welcome mail sent')
            current_site = get_current_site(request)
            domain = current_site.domain 
            print(current_site)
            print('domain:', domain)                
            token = token_activation(username, password1)
            print('return from tokens.py:', token)
            url = str(token)
            surl = get_surl(url)
            z = surl.split("/")
            print(z[2])
            mail_subject = "Activate your account clicking on the link below"
            message = render_to_string('email_validation.html', {
                    'user': user_created.username,
                    'domain': domain,
                    'surl': z[2]
                })
            # send_mail(mail_subject, message, from_mail, to_list, fail_silently=True)
            message.send()
            print('confirmation mail sent')
            return HttpResponse('Please confirm your email address to complete the registration')

        except Exception as e:
            messages.error(request, "user creation failed")
            smd["success"] = False
            smd["message"] = "last return"
            return HttpResponse(json.dumps(smd), status=400)

    # def post(self, request):

    #     username = request.data['username']
    #     email = request.data['email']
    #     password = request.data['password1']
    #     password2 = request.data['password2']
    #     print(email)


    #     smd = {
    #         'success': False,
    #         'message': "not registered yet",
    #         'data': [],
    #     }

    #     # try:
    #     #     validate_email(email)
    #     # except Exception:
    #     #     smd['message'] = "please enter vaild email address"
    #     #     return HttpResponse(json.dumps(smd))


    #     if username == "" or email == "" or password == "":
    #         smd['message'] = "one of the details missing"
    #         logger.error("one of the details missing logging in")
    #         return HttpResponse(json.dumps(smd), status=400)

    #     elif User.objects.filter(email=email).exists():
    #         smd['message'] = "email address is already registered "
    #         logger.error("email address is already registered  while logging in")
    #         return HttpResponse(json.dumps(smd), status=400)

    #     else:
    #         try:
    #             user_created = User.objects.create_user(username=username, email=email, password=password, is_active=False)
    #             print(user_created)
    #             user.save()

    #             if user_created :
    #                 current_site = get_current_site(request)
    #                 mail_subject = 'Activate your blog account.'
    #                 message = render_to_string('acc_active_email.html', {
    #             'user': user,
    #             'domain': current_site.domain,
    #             'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    #             'token':account_activation_token.make_token(user),
    #                 })
    #             # to_email = user('email')
    #             # print(to_email)
    #             to_list = [user_created.email]
    #             print(user_created.email)
    #             send_mail(sub, msg, from_mail, to_list, fail_silently=True)
    #             # emailll = EmailMessage(
    #             #         mail_subject, message, to=[to_email]
    #             #     )
    #             # print(emailll)
    #             email.send()
    #                 # token = token_activation(username, password)
    #                 # url = str(token)
    #                 # surl = get_surl(url)
    #                 # z = surl.split("/")

    #                 # mail_subject = "Activate your account by clicking below link"
    #                 # mail_message = render_to_string('email_validation.html', {
    #                 #     'user': user_created.username,
    #                 #     'domain': get_current_site(request).domain,
    #                 #     'surl': z[2]
    #                 # })
    #                 # print(mail_message)
    #                 # recipient_email = user_created.email
    #                 # email = EmailMessage(mail_subject, mail_message, to=[recipient_email])
    #                 # email.send()
    #                 # smd = {
    #                 #     'success': True,
    #                 #     'message': 'please check the mail and click on the link  for validation',
    #                 #     'data': [token],
    #                 # }
    #                 # logger.info("email was sent to %s email address ", username)
    #             return HttpResponse(json.dumps(smd), status=201)
    #         except Exception as e:
    #             smd["success"] = False
    #             smd["message"] = "username already taken"
    #             logger.error("error: %s while loging in ", str(e))
    #             return HttpResponse(json.dumps(smd), status=400)

# def activate(request, surl):
    
#     try:
#         tokenobject = ShortURL.objects.get(surl=surl)
#         token = tokenobject.lurl
#         decode = jwt.decode(token, settings.SECRET_KEY)
#         username = decode['username']
#         user = User.objects.get(username=username)

#         if user is not None:
#             user.is_active = True
#             user.save()
#             messages.info(request, "your account is active now")
#             return redirect('login')
#         else:
#             messages.info(request, 'was not able to sent the email')
#             return redirect('registration')
    


    # except KeyError:
    #     messages.info(request, 'was not able to sent the email')
    #     return redirect('registration')
    
    # except ExpiredSignatureError:
    #     messages.info(request, 'activation link expired')
    #     return redirect('registration')
    
    # except Exception:
    #     messages.info(request, 'activation link expired')
    #     return redirect('registration')
                    

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')