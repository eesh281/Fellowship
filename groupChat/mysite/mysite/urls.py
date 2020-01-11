from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from snippets.views import Login, Registrations, activate, ForgotPassword, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from chat.views import index, room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', Login.as_view(), name='login'),
    path('activate/<slug:surl>/', activate, name='activate'),
    path('registration/', Registrations.as_view(), name="registration"),
    path('forgot_password/', ForgotPassword.as_view(),name="forgot_Password"),
    # path('activate/<surl>/', views.activate, name="activate"),
    path('reset_password/<slug:surl>/', reset_password, name="reset_password"),
    path('resetpassword/<user_reset>', ResetPassword.as_view(), name="resetpassword"),
    # path('logout/', views.Logout.as_view() ,name="logout"),
    path('session/', session),   

    path('chat/', include('chat.urls')),
]