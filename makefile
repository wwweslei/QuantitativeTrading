deploy:
	git push heroku main
log:
	heroku logs --tail
reqtxt:
	poetry export -f requirements.txt --output requirements.txt