from django.conf import settings
from django.shortcuts import redirect

from django.shortcuts import render
from blog.models import *

from systemd.manager import Manager
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def stronaglowna(request):

	#if not request.user.is_authenticated():

		#return redirect('blog.views.logowanie')

	systemd_manager = Manager()

	uslugi = Usluga.objects.all()

	# dla kazdej uslugi dodaj x.activeState
	for x in uslugi:
		if x.plik_service: #jeśli jest okreslony plik oslugi podany 
			unit = systemd_manager.get_unit(x.plik_service)
			x.activeState = unit.properties.ActiveState
			
	kontekst = {
		'lista_uslug': uslugi
	}
	systemd_manager.unsubscribe()
	return render(request, 'main.html', kontekst)


def logowanie(request):
	if request.method == 'POST':
		#import pdb; pdb.set_trace()
		user = authenticate(
			username=request.POST.get('id_username', '').strip(),
			password= request.POST.get('id_password', ''),
			)

		

		if user is None:
			kontekst = {
			'ukryty': 'Nieprawidłowa nazwa użytkownika lub hasło'
			}
			return render(request, 'registration/login.html', kontekst)
			#messages.error(request, u'blad logowania')
		else:
			if user.is_active:
				login(request, user)

				if next in request.GET:
					return redirect(request.GET['next'])
				else:
					return redirect('blog.views.stronaglowna')
			else:
				messages.error(request, u'User is not active.')

				#return render_to_response('registration/login.html')
	return render(request, 'registration/login.html')
