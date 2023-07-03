deploy:
	git push heroku main

h_log:
	heroku logs --tail

h_bash:
	heroku run bash

txt:
	poetry export -f requirements.txt --output requirements.txt

user:
	poetry run python manage.py createsuperuser
h_user:
	heroku run python manage.py createsuperuser
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
	python manage.py migrate --run-syncdb

h_migrate:
	heroku run python manage.py makemigrations core
	heroku run python manage.py migrate
run:
	poetry run python manage.py runserver_plus

test:
	poetry run pytest -vv

shell:
	poetry run python manage.py shell_plus

note:
	poetry run python manage.py shell_plus --notebook

server:
	waitress-serve --listen=*:8000 quantitativeTrading.wsgi:application
co:
	poetry run python manage.py collectstatic --noinput
css:
	poetry run python manage.py sass-compiler
docker:
	sudo systemctl start docker
docker-up:
	docker compose -f "docker-compose.yml" up -d --build
db:
	pgcli postgres://postgres:fdjk@localhost:5432/quantitativeTrading
