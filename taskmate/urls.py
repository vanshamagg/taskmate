"""taskmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from todolist_app import views as todolist_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_view.index, name='index'),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('about', todolist_view.about, name='about'),
    path('contact', todolist_view.contact, name='contact'),
    path('random/<int:id>', todolist_view.random_task , name ='random_task'),
    

]