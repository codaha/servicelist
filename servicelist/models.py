from django.db import models

class ItemManager(models.Manager):

	def next_number(self):
		return self.count() + 1





from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Project 2501')
    allow_anonymous = models.BooleanField(default=False)
    mail = models.EmailField(blank=True)

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


from adminsortable.models import Sortable
class Service(Sortable):

	class Meta(Sortable.Meta):
		pass
	name = models.CharField(max_length=100)
	url = models.URLField(blank=True)
	#service_file = models.ForeignKey(ServiceFile)
	description = models.CharField(max_length=1000, blank=True)
	
	def __str__(self):
		return self.name



class ServiceFile(models.Model):
	service_file = models.CharField(max_length=100)
	service = models.ForeignKey(Service)
	def __str__(self):
		return self.service_file

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
 
