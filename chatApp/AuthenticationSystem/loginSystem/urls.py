from django.urls import path
# from . import views
# from django.views.generic import TemplateView
# from django.conf.urls import url

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('', views.login, name = 'users-login'),
    # path('login/', views.Login.as_view(), name="login"),
    
    # path('registration/', views.Registration.as_view(), name="registration"),
    # path('activate/<surl>/', views.activate, name="activate"),
    
    # path('forgotpassword',views.ForgotPassword.as_view(), name="forgotpassword"),
    # path('reset_password/<surl>/', views.reset_Password, name="reset_password"),
    # path('resetpassword/<user_reset>/', views.ResetPassword.as_view(), name="resetpasswordview"),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]

