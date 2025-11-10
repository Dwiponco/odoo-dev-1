WEB_DB_NAME = odoo_development
DOCKER = docker
DOCKER_COMPOSE = ${DOCKER} compose
CONTAINER_ODOO = odoo
CONTAINER_DB = odoo-postgres

help:
	@echo "Available commands:"
	@echo "start           		- start the containers"
	@echo "stop            		- stop the containers"
	@echo "restart         		- restart the containers"
	@echo "console         		- open the console of the containers"
	@echo "logs            		- show the logs of the containers"
	@echo "psql            		- open the psql of the database"
	@echo "logs-db         		- show the logs of the database"
	@echo "logs-odoo       		- show the logs of the odoo"
	@echo "logs-all        		- show the logs of all the containers"
	@echo "addons <addon_name>  - restart instance and update the addons"

addon:
	$(call upgrade_addon,$(word 2, $(MAKECMDGOALS)))

define upgrade_addon
	${DOCKER} exec -it ${CONTAINER_ODOO} odoo --db_host=${CONTAINER_DB} -d $(WEB_DB_NAME) -r $(CONTAINER_ODOO) -w $(CONTAINER_ODOO) -u $(1)
endef

start:
	${DOCKER_COMPOSE} up -d

stop:
	${DOCKER_COMPOSE} down

restart:
	${DOCKER_COMPOSE} restart

console:
	${DOCKER} exec -it ${CONTAINER_ODOO} bash

logs:
	${DOCKER} logs -f ${CONTAINER_ODOO}

psql:
	${DOCKER} exec -it ${CONTAINER_DB} psql -U ${CONTAINER_ODOO} -d ${WEB_DB_NAME}

logs-db:
	${DOCKER} logs -f ${CONTAINER_DB}

logs-odoo:
	${DOCKER} logs -f ${CONTAINER_ODOO}

logs-all:
	${DOCKER} logs -f ${CONTAINER_ODOO} ${CONTAINER_DB}

.PHONY: help start stop restart console logs logs-db logs-odoo logs-all addon