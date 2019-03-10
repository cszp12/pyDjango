#为应用城徐users定义城徐
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from django.contrib.auth import login
from django.urls import path

from . import views

app_name ='users'
urlpatterns = [
	#登陆
	#path(r'^login/$', login, {'template_name' : 'users/login.html'}, name='login'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
	#注销
	path('logout/', views.logout_view, name='logout'),
	#注册
	path('register/', views.register, name='register'),
]
