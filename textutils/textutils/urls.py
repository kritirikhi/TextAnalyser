"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('performOperationAction/',views.performOperationAction,name='performOperationAction'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('error/',views.error,name='error'),
    path('performoperation/',views.performoperation,name='performoperation'),
    path('analysecharacters/',views.analysecharacters,name='analysecharacters'),
    path('analysecharaction/',views.analysecharaction,name='analysecharaction'),
    path('eachcharresult/',views.eachcharresult,name='eachcharresult'),
    path('funtext/',views.funtext,name='funtext'),
    path('textfunaction/',views.textfunaction,name='textfunaction'),
    path('textfunoutput/',views.textfunoutput,name='textfunoutput'),
    path('extracturl/',views.extracturl,name='extracturl'),
    path('extracturlaction/',views.extracturlaction,name='extracturlaction'),
    path('extracturloutput/',views.extracturloutput,name='extracturloutput'),
]
