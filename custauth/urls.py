from django.urls import path
from . import views

appname="auth"
urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('login/', views.login_page, name="login_page"),
    path('loginrequest/', views.login_request, name="login"),
    path('logout/', views.user_logout, name="logout"),
]