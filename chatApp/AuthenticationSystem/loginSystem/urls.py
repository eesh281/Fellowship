from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.user_registration, name='login'),
    # url(r'^registration/$', registration, name='registration'),
    # url(r'^login/$', login, name='login'),
]

