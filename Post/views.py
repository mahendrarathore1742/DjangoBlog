from django.shortcuts import render,redirect
from Post.form import Datapost
from django.contrib.auth import authenticate,login,logout;
from django.views.generic import ListView
from Post.models import PostData
from django.views.generic.detail import DetailView
from django.contrib import messages
import re;

def newpost(request):
	if request.method=='POST':
		form=Datapost(request.POST)
		if form.is_valid(): 
			form.save();
		else:
			messages.error(request,'You should check in on some of those fields below!')
			return redirect('/admin/newpost')
		return redirect('/listofallpost')
	else:
		form=Datapost();
		return render(request,'newpost.html',{"form":form})


class listofalldata(ListView):
	template_name='listofallpost.html';
	queryset=PostData.objects.all()

class Displaypostdata(DetailView):
	template_name='CompleteDetail.html';
	queryset=PostData.objects.all()
	
	


