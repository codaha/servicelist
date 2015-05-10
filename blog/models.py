from django.db import models

class ItemManager(models.Manager):

	def next_number(self):
		return self.count() + 1


class Usluga(models.Model):
	nazwa = models.CharField('nazwa usługi', max_length=100)
	adres = models.URLField('adres URL', blank=True)
	plik_service = models.CharField('nazwa pliku service', max_length=100, blank=True)
	opis = models.CharField('opisik', max_length=1000, default="")

	#kolejnosc = models.IntegerField(default=lambda: Usluga.get_next_number())
	kolejnosc = models.IntegerField(default=0)
	@classmethod
	def get_next_number(cls):
		return cls.objects.count() + 1

#na liscie admina wyswietlaj tytulujac nazwa
	def __str__(self):
		return self.nazwa

	class Meta:	
		verbose_name_plural = "usługi"
		verbose_name = "usługa"