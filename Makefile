
install: venv
	. venv/bin/activate && pip install -r requirements.txt

venv:
	virtualenv venv

db:
	createdb -h localhost -U postgres -O postgres -E utf-8 ddjj
	. venv/bin/activate && python ddjj/manage.py syncdb && python ddjj/manage.py migrate

dropdb:
	dropdb -h localhost -U postgres ddjj

resetdb: dropdb db

.PHONY: install db
