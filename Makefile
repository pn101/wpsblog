migrate:
	- python wpsblog/manage.py makemigrations bitly users posts wpsblog
	- python wpsblog/manage.py migrate
