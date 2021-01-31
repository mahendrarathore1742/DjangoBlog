from django.shortcuts import render,HttpResponse
from Post.models import PostData
from django.contrib import messages
from django.views.generic import ListView
from .models import Category;

from Post.models import PostData

# Create your views here.
def home(requset):
	newpost=PostData.objects.filter(published=True).order_by('-published_date')[0:3]
	return render(requset,'home.html',{'newpost':newpost})
  
class Topnews(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='Top News')

class Scifi(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='SCI FI')

class Topwebseries(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='Top Web series')
 
class Universe(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='Universe' )

class Galaxies(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='galaxy')

class WhirlpoolGalaxies(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='WhirlpoolGalaxies')
 
class BigBang(ListView):
	template_name='allpost.html';
	def get_queryset(self):
		return PostData.objects.filter(Category__name='Big Bang')
 

def Search(request):
	query=request.GET['query']
	if len(query)>78:
		allpost=PostData.objects.none();
	else:
		allpostTitle=PostData.objects.filter(Title__icontains=query);
		allpostcontent=PostData.objects.filter(Content__icontains=query);
		allpost=allpostTitle.union(allpostcontent)
	if allpost.count()==0:
		 messages.error(request, ' No search Result Found try again')
	if query=="":
		messages.error(request, 'Enter the value what you want!')
		allpost=PostData.objects.none();
	data={'allpost':allpost,'query':query}

	return render(request,'search.html',data) 
	
	
	
	
	
	
	
