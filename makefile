deploy:
	git push heroku main

h_log:
	heroku logs --tail

txt:
	poetry export -f requirements.txt --output requirements.txt

user:
	poetry run python manage.py createsuperuser
h_user:
	heroku run python manage.py createsuperuser
migrate:
	poetry run python manage.py makemigrations core
	poetry run python manage.py migrate core

h_migrate:
	heroku run python manage.py migrate
run:
	poetry run python manage.py runserver_plus

test:
	poetry run python manage.py test core.tests  

shell:
	poetry run python manage.py shell_plus