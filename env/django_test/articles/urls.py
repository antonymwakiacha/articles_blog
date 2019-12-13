from django.contrib import admin
from django.conf.urls import url,include

from .models import Article
#from .views import article,articles
from articles import views

urlpatterns=[
	url(r'^all/$',views.articles,name='articles'),
	url(r'^get/(?P<article_id>\d+)/$',views.article,name='article'),
	]