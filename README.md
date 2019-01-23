# Budget Tool
A Django / Docker tool that will allow for the tracking of user controlled budgets.

## Getting Started
1. Download the repo
1. Ensure your virtual environment matches that of the Pipfile
1. Install Docker Desktop if needed, then spin up the container with docker-compose up
1. Currently you will need to create a superuser by bashing into the docker container. Once logged into the site as admin you will be able to add / remove budgets. 

## Architecture
Python, Docker, Django

## TODO
1. Add user ability to create transactions.
1. Add user ability to remove transactions.
1. Fix up any testing errors.
