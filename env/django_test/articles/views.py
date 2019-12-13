from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import Context
from articles import models
from articles.models import Article

def hello(request):
	return HttpResponse("hello there")

def home(request):
	return HttpResponse("am home")

def hello_template(request):
	name='Tony'
	return render(request,'hello.html',{'name':name})

class HelloTemplate(TemplateView):
	template_name="hello_class.html"
	def get_context_data(self,**kwargs):
		context=super(HelloTemplate,self).get_context_data(**kwargs)
		context['name']='Stark'
		return context

def articles(request):
	return render(request,'articles.html',{'articles':Article.objects.all()})

def article(request,article_id=1):
	return render(request,'article.html',{'article':Article.objects.get(id=article_id)})
 