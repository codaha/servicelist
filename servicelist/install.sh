#!/bin/bash
set -x; #echo on

virtualenv venv;
source venv/bin/activate;
pip install django django-admin-sortable django-axes django-solo python-systemd pytz 2to3;
2to3 -w venv/lib/python3.4/site-packages/systemd;
wget http://dbus.freedesktop.org/releases/dbus-python/dbus-python-1.2.0.tar.gz;
tar xfv dbus-python-1.2.0.tar.gz;
cd dbus-python-1.2.0;
sciezk="$PWD/venv";
deactivate;
./configure --prefix=sciezk;
make;
make install;
cd ../;
./manage.py makemigrations;
./manage.py migrate;
./manage.py createsuperuser;