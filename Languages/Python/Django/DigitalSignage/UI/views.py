from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout , REDIRECT_FIELD_NAME
from django.views.generic import View, RedirectView
from .models import MainDB, defaultDB
from .forms import UserForm


class UserFormView(View):
	form_class=UserForm
	template_name='UI/registrationform.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})
	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			user=form.save(commit=False)

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('UI:index')
		return render(request,self.template_name,{'form':form})

class IndexView(generic.ListView):
	model=defaultDB
	template_name='UI/display.html'

	def get_queryset(self):
		return (defaultDB.objects.all())

class DetailView(generic.DetailView):
	model=MainDB
	template_name='UI/detail.html'

class MainDBCreate(CreateView):
	model=MainDB
	fields=['s_no','address','auto_date','timeA','timeB']

class MainDBUpdate(UpdateView):
	model=MainDB
	fields=['address','auto_date','timeA','timeB']

class MainDBDelete(DeleteView):
	model=MainDB
	success_url=reverse_lazy('UI:index')


def logout_view(request):
	template='UI/logout.html'
	return redirect(request,template, {})