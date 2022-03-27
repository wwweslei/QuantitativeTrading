deploy:
	git push heroku main
log:
	heroku logs --tail
txt:
	poetry export -f requirements.txt --output requirements.txt