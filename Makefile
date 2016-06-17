migrate:
	- python wpsblog/manage.py makemigrations bitly users posts wpsblog
	- python wpsblog/manage.py migrate
test:
	- python wpsblog/manage.py test users posts bitly wpsblog -v2
pep:
	- pep8 .
