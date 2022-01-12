build:

	docker compose -f docker-compose_dev.yml up --build

tests:

	docker compose -f docker-compose_dev.yml run tdd-services pytest -vv

aeirich init:

	docker compose -f docker-compose_dev.yml run tdd-services aerich init -t app.db.TORTOISE_ORM

aeirich init-db:

	docker compose -f docker-compose_dev.yml run tdd-services aerich init-db

.PHONY: \
	build \
	tests \
	aeirich init \
	aeirich init-db \
