from django import forms

class new_service(forms.Form):
	nazwa = forms.CharField()
	adres = forms.URLField(required=False)
	plik_service = forms.CharField(required=False)
	#wywala błąd
	#opis = forms.Textarea(required=False)
	#nie renderuje
	opis = forms.Textarea()