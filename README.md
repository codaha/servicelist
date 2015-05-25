# servicelist

Simple tool for your VPS, displays list of avaible services to show world your content.

Written in django and bootstrap.

Project requies dbus-glib library! Install it rom your system repo.

Requied python libries are included in VitualEnv. These are:

django
basic of this project

django-axes
for managing failed login attempts

pytz 
dependency of django-axes

systemd_manager
for managing service files. This was translated from python 2 to python 3 using 2to3

dbus-python
Dependency of systemd_manager. This was compiled mannually from source because some problems with installing it by pip

django-admin-sortable
For drag and drop sorting of iteams in admin panel


