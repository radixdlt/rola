up:
	docker-compose up

migrate:
	docker exec -it rola npx prisma migrate dev

generate:
	docker exec -it rola npx prisma generate

up-build:
	docker-compose up --build

up-prod:
	docker-compose -f ./docker-compose.prod.yml up --build

up-test:
	docker-compose -f ./docker-compose.yml -f ./docker-compose.test.yml up

up-test-build:
	docker-compose -f ./docker-compose.yml -f ./docker-compose.test.yml up -d --build

logs:
	docker-compose logs -f --tail 100

down: 
	docker-compose down

down-test: 
	docker-compose -f ./docker-compose.yml -f ./docker-compose.test.yml down