from django.db import models

class ItemManager(models.Manager):

	def next_number(self):
		return self.count() + 1


from adminsortable.models import Sortable
class Service(Sortable):

	class Meta(Sortable.Meta):
		pass
	name = models.CharField(max_length=100)
	url = models.URLField(blank=True)
	service_file = models.CharField(max_length=100, blank=True)
	description = models.CharField(max_length=1000, default="")
	
	def __str__(self):
		return self.name

from django.contrib.auth.models import User


#dodaje uprawniania dla usera
class Permission(models.Model):
	user = models.OneToOneField(User)
 
	ADMIN = 'Ad'
	UZYTKOWNIK = 'Us'
 	
	typy = (
		(ADMIN, 'Admin'),
		(UZYTKOWNIK, 'Uzytkownik'),
		)
	Permissions = models.CharField(max_length=2, choices=typy,
		default=UZYTKOWNIK)
 
