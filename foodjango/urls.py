from django.urls import path
from foodjango import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('login/signup/', views.signup, name='signup'),
    path('login/signup/register', views.register, name='register'),
    path('login/menu', views.menu, name='menu'),
    path('login/validate_user', views.validate_user, name='validate_user'),
    # path('login/validate_user', views.validate_user, name='validate_user'),
]
