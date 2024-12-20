DC = docker compose
EXEC = docker exec
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest $(path)

.PHONY: test-cov
test-cov:
	${EXEC} ${APP_CONTAINER} pytest --cov=$(path)

.PHONY: lint
lint:
	${EXEC} ${APP_CONTAINER} isort . --check-only --diff
