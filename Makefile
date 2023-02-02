serve:
	docker-compose up -d
stop:
	docker-compose down
test:
	docker-compose up -d && docker-compose run todo-app pytest && docker-compose down