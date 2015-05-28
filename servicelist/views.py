#django
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

#authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


### from this project
from servicelist.models import *
from django.conf import settings

#external libraries
if(settings.INITSYSTEM == "systemd"):
	from systemd.manager import Manager
if(settings.INITSYSTEM == "openrc"):
	pass


config = SiteConfiguration.get_solo()
config = SiteConfiguration.objects.get(pk=1)

if(config.allow_anonymous):
	def do_nothing(funct):
		return funct
		
	login_if_required = do_nothing
else:
	login_if_required = login_required


@login_if_required
def services(request):
	if(settings.INITSYSTEM=="systemd"):
		systemd_manager = Manager()
	lista_baza = Service.objects.all()
	lista_plik = ServiceFile.objects.all()
	# dla kazdej uslugi dodaj x.activeState
	for x in lista_baza:
		if(settings.INITSYSTEM=="systemd"):
			matching_services = ServiceFile.objects.filter(service=x)
			if matching_services:
				matching_services_names=[]
				for y in matching_services:
					try:
						unit = systemd_manager.get_unit(y.service_file)
						y.activeState = unit.properties.ActiveState
					except:
						y.activeState= 'none'
	
					ser = {y.service_file: y.activeState}
					matching_services_names.append(ser)
					#print(matching_services_names)
	
				x.service_state = matching_services_names
	
			#if x.service_file: #jeśli jest okreslony plik oslugi podanyistnieje w systemie
			#	unit = systemd_manager.get_unit(x.service_file)
			#	x.activeState = unit.properties.ActiveState
		if(settings.INITSYSTEM=="openrc"):
			pass


	kontekst = {
		'service_list': lista_baza
	}
	#print(kontekst)
	if(settings.INITSYSTEM == "systemd"):
		systemd_manager.unsubscribe()
	return render(request, 'main.html', kontekst)


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
	return redirect('login')
