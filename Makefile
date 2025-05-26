.PHONY: run test migrate upgrade
PYTHONPATH=. pytest

run:
	FLASK_APP=app:create_app flask run

test:
	pytest

migrate:
	FLASK_APP=app:create_app flask db migrate

upgrade:
	FLASK_APP=app:create_app flask db upgrade