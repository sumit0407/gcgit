from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [


path("",views.Dashboard,name="dashboard"),
path("AdminSigiIn",views.admin_signin,name="signin"),
path("AdminSignUp",views.admin_signup,name="signup"),


path("AdminSignUser",views.AdminSignUp,name="adminsignup"),

path("AdminSignupUser",views.AdminSigiIn,name="adminsignin"),

]