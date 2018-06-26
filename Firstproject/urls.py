"""Firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from mainsite.views import homepage,showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homepage),
    url(r'^post/(\w+|.+)$', showpost), 
    #把所有post/开头的网址的后面字符串都找出来,单纯的\w+找不到含有空格的,
    # 小括号表示是一组要取出的参数，在小括号中取出来的内容会自动以参数的方式的方式传送到后面的函数里，
    
]
