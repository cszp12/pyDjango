from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
	#注销用户
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

# Create your views here.


def register(request):
	#注册新用户
	if request.method != 'POST':
		#显示空的注册表单
		form = UserCreationForm()
	else:
		#处理写好的表单
		form = UserCreationForm(data=request.POST)
		print(request.POST)
		print(form.is_valid)
		if form.is_valid():
			new_user = form.save()
			#让用户自动登录
			authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form' : form}
	return render(request, 'users/register.html', context)