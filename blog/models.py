from django.db import models

class Usluga(models.Model):
	nazwa = models.CharField('nazwa usługi', max_length=100)
	adres = models.URLField('adres URL')
	plik_service = models.CharField('nazwa pliku service', max_length=100)

	def __str__(self):
		return self.nazwa

	class Meta:	
		verbose_name_plural = "usługi"
		verbose_name = "usługa"