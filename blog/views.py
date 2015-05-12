#django
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

#logowanie
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#biblioteki zewnetrzen
from systemd.manager import Manager

### projekt
from .forms import *
from blog.models import *




from django.conf import settings
if(settings.ALLOW_ANONYMOUS):
	def nic(funct):
		return funct
		
	corobic = nic

else:
	corobic = login_required


#funkcja używna przez liste uslug  podstrone edycji
def lista(request):

	systemd_manager = Manager()


	lista_baza = Usluga.objects.all()

	# dla kazdej uslugi dodaj x.activeState
	for x in lista_baza:
		try: #nieistniejacy plik service spowoduje błąd
			if x.plik_service: #jeśli jest okreslony plik oslugi podanyistnieje w systemie
				unit = systemd_manager.get_unit(x.plik_service)
				x.activeState = unit.properties.ActiveState
		except:
			pass

	lista_baza=sorted(lista_baza, key=lambda x: x.kolejnosc)
	kontekst = {
		'lista_uslug': lista_baza
	}
	systemd_manager.unsubscribe()
	return kontekst

#podstrona edycji
@corobic
def uslugi(request):
	
	k=lista(request)
	k.update({'coto': 'lista'})
	
	return render(request, 'main.html', k)


#lista zwyklych uslug
@corobic
def edycja(request):
	
	k=lista(request)
	k['coto'] = 'edycja'
	return render(request, 'main.html', k)


@corobic
def dodajnowy(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = Nowy(request.POST)
		# check whether it's valid:
		if form.is_valid():
			Usluga(nazwa=request.POST.get('nazwa'), adres=request.POST.get('adres'), plik_service=request.POST.get('plik_service')).save()
			#p.save()
			return HttpResponse("Dodano")

# if a GET (or any other method) we'll create a blank form
	else:
		form = Nowy()


	return render(request, 'dodaj.html', {'form': form})
	#return HttpResponse("empty")
from axes.decorators import watch_login

#potrzebne poniewaz nie uzywam standardowego view django login
@watch_login
def logowanie(request):
	#jeśli strona jest przeładowywana w celu logowania
	if request.method == 'POST':
		#import pdb; pdb.set_trace()
		user = authenticate(
			username=request.POST.get('id_username', '').strip(),
			password= request.POST.get('id_password', ''),
			)

		
		#jeśli złe dane logowania
		if user is None:
			kontekst = {
			'ukryty': 'Nieprawidłowa nazwa użytkownika lub hasło'
			}
			return render(request, 'registration/login.html', kontekst)
		else:
			#jeśli dale logowania ok
			if user.is_active:
				login(request, user)
				#jeśli jest info gdzie przekirować z strony logowania
				if next in request.POST:
					return redirect(blog.views.request.POST['next'])#TODO
				#jeśli user wszedl bezposrednio na stronę logowania
				else:
					return redirect('blog.views.uslugi')
	#jeśli user jest już zalogowany
	if request.user.is_authenticated():
		return redirect('blog.views.uslugi')
	#jeśli strona loginu jest otwierana w celu wpisania danych dopiero
	else:
		return render(request, 'registration/login.html')
def wyloguj(request):
	logout(request)
	return redirect('blog.views.logowanie')

#inaczej blad 403 przy ajax
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def kolejnosc(request):
	#pass
	
	if request.method == 'POST':
		#otrzymujemy string z kolejnascia  na lisciekolejnych elementow oznaczonych numerami id w bazie danych
		#usuwamy "pozycja" i dzielimy string na liste
		lista= request.POST.get('lista', '').replace("pozycja[]=", "").split('&')

		#lista_baza = Usluga.objects.all()

		#import pdb; pdb.set_trace()

		for nr, x in enumerate(lista, start=1):
			pozycja = Usluga.objects.get(id=x)#.save(kolejnosc=nr)
			pozycja.kolejnosc=nr
			pozycja.save()
			
		#print(lista)