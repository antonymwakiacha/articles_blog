"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from articles import views,urls
from django.conf.urls import url,include
from articles.views import HelloTemplate

urlpatterns = [
	re_path(r'^articles/',include('articles.urls')),
    path('admin/', admin.site.urls),
    url(r'^hello/$',views.hello,name='hello'),
    path('',views.home,name='home'),
    #url(r'^/$',views.home,name='home')
    url(r'^hello_template/$',views.hello_template,name="hello_template"),
   	url(r'^hello_class/$',HelloTemplate.as_view(),name='hello_class'),
    #path('articles/',articles.urls),

	  
 ]

# urlpatterns=[
# 	#(r'^articles/',include('articles.urls')),
# 	path('articles/',include('articles.urls')),
# ]
 # path('articles/',include('articles.urls')),