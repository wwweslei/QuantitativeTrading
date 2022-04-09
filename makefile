deploy:
	git push heroku main
log:
	heroku logs --tail
txt:
	poetry export -f requirements.txt --output requirements.txt
user:
	poetry run python manage.py createsuperuser

migrate:
	poetry run python manage.py makemigrations core
	poetry run python manage.py migrate core
run:
	poetry run python manage.py runserver_plus