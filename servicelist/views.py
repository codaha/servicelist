#django
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

#authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#external libraries
from systemd.manager import Manager

### from this project
from .forms import *
from servicelist.models import *



from django.conf import settings
if(settings.ALLOW_ANONYMOUS):
	def do_nothing(funct):
		return funct
		
	login_if_required = do_nothing

else:
	login_if_required = login_required




@login_if_required
def services(request):
	systemd_manager = Manager()
	lista_baza = Service.objects.all()

	# dla kazdej uslugi dodaj x.activeState
	for x in lista_baza:
		try: #nieistniejacy plik service spowoduje błąd
			if x.plik_service: #jeśli jest okreslony plik oslugi podanyistnieje w systemie
				unit = systemd_manager.get_unit(x.plik_service)
				x.activeState = unit.properties.ActiveState
		except:
			pass

	lista_baza=sorted(lista_baza, key=lambda x: x.position)
	kontekst = {
		'service_list': lista_baza
	}
	systemd_manager.unsubscribe()
	
	return render(request, 'main.html', kontekst)



@login_if_required
def add_service(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = new_service(request.POST)
		# check whether it's valid:
		if form.is_valid():
			Service(name=request.POST.get('nazwa'), url=request.POST.get('adres'), service_file=request.POST.get('plik_service')).save()
			#p.save()
			return HttpResponse("Dodano")

# if a GET (or any other method) we'll create a blank form
	else:
		form = new_service()


	return render(request, 'add_service.html', {'form': form})
	#return HttpResponse("empty")
from axes.decorators import watch_login

@watch_login
def login_view(request):
	#when page is requested
	if request.method == 'POST':
		user = authenticate(
			username=request.POST.get('id_username', '').strip(),
			password= request.POST.get('id_password', ''),
		)
		
		#when wrong credentials provided
		if user is None:
			kontekst = {
			'ukryty': 'Wrong username or password'
			}
			return render(request, 'registration/login.html', kontekst)
		else:
			#when credentials are good
			if user.is_active:
				login(request, user)
				if next in request.POST:
					#when user was redirected here, redirect him back after authorization
					return redirect(servicelist.views.request.POST['next'])#TODO
				else:
					return redirect('servicelist.views.services')
	if request.user.is_authenticated():
		return redirect('servicelist.views.services')
	#unfilled form is requested to scarcely provide credentials
	else:
		return render(request, 'registration/login.html')
def logout_view(request):
	logout(request)
	return redirect('servicelist.views.login_view')

#without this there will be 403 error from ajax
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def ajax_order(request):
	if request.method == 'POST':
		#we should get string with order of elements on the list marked with id numbers from db
		#we remove "order" and strip string to list
		list= request.POST.get('lista', '').replace("pozycja[]=", "").split('&')
		for nr, x in enumerate(list, start=1):
			s = Service.objects.get(id=x)
			s.position=nr
			s.save()