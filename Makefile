build:
	docker build -t mvplanding -f Dockerfile . 

run:
	docker run --env-file ./src/.env -p 8201:8000 -p 8200:80 --name mvplanding --rm  mvplanding

stop:
	docker stop mvplanding

push:
	docker build --platform=linux/amd64 -t codingforentrepreneurs/mvplanding:latest -f Dockerfile . 
	docker push codingforentrepreneurs/mvplanding --all-tags

runserver:
	cd src && ../venv/bin/python manage.py runserver

requirements:
	venv/bin/pip-compile --output-file src/requirements.txt --upgrade src/requirements/requirements.in
	venv/bin/python -m pip install -r src/requirements.txt
