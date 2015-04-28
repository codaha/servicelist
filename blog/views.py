from django.http import HttpResponse

from django.shortcuts import render
from blog.models import *

from systemd.manager import Manager

def stronaglowna(request):
	systemd_manager = Manager()

	uslugi = Usluga.objects.all()

	# dla kazdej uslugi dodaj x.activeState
	for x in uslugi:
		if x.plik_service:
			unit = systemd_manager.get_unit(x.plik_service)
			x.activeState = unit.properties.ActiveState
	kontekst = {
		'lista_uslug': uslugi
	}
	systemd_manager.unsubscribe()
	return render(request, 'main.html', kontekst)



#def stronaglowna(request):
	#return HttpResponse('super lista')