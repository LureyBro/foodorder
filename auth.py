from django.shortcuts import redirect

# to check if the user is logged in or not

def unauthenticated_user(view_function):
	def wrapper_function(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_function(request,*args,**kwargs)
	return wrapper_function

# give access to admin pages if request comes from admin
# request is from normal user redirect to user dashboard

def admin_only(view_function):
	def wrapper_fuction(request,*args,**kwargs):
		if request.user.is_staff:
			return view_function(request,*args,**kwargs)
		else:
			return redirect('/')
	#return wrapper_function

# give access to user page if request comes from naomal user
# if request is from admin then redirect ro admin dashboard

def user_only(view_function):
	def wrapper_function(request,*args,**kwargs):
		if request.user.is_staff:
			return redirect('/dashboard')
		else:
			return view_function(request,*args,**kwargs)
	return wrapper_function

	