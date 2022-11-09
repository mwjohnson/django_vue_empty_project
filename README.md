# Statuses

## Circle-CI


# Components
This project serves as a template contains:
 - nginx
 - Vue Client
 - Django Rest Framework API
 - Postgres database
 - RabbitMQ broker
 - Celery worker (based from API)
 - Redis cache
 - Flower task monitor
 - Docker-compose based launching/environment

TODO: Add diagram showing connections/ports between containers

# Duplicating the Template Repo

1. Create a bare clone:

`git clone --bare https://github.com/exampleuser/project_template.git`

2. Mirror-push to new repository:

`$ cd old-repository.git`

`$ git push --mirror https://github.com/exampleuser/<new-repository>.git`

3. Remove the temporary local repository we created in step 1:

`cd ..`

Linux: `rm -rf project_template.git`

Widnows: `rm C:\path\to\project_template.git\ -Recurse -Force` **BE CAREFUL!**

4. Clone the new repository:

`git clone https://<new-repository>.git`

[help.github](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)

# How to Launch with Docker Compose

## Step One:

From folder: `<git cloned directory>\project_template\api>`

Run the command: `docker build -t api .` This will build the __**api**__ docker image.

You should see the following output if the image build was successful: `Successfully tagged api:latest`

### Important Note:
Launching docker-compose directly from `<git cloned directory>/project_template/` will try to
pull the docker-image from the docker repository which is not the desired action.

## Step Two:
Next from folder: `<git cloned directory>\project_template\client>`

Run the command: `docker build -t client .` This will build the __**client**__ docker image.

You should see the following output if the image build was successful: `Successfully tagged client:latest`

## Step Three:
Next from folder: `<git cloned directory>\project_template\nginx>`

Run the command: `docker build -t nginx .` This will build the __**nginx**__ docker image.

You should see the following output if the image build was successful: `Successfully tagged nginx:latest`

## Step Four (Final Step):

From Folder: `<git cloned directory>/project_template/docker-compose/development/`

Run the command: `docker-compose up`

You should see a wall of text as each of the seven containers comes online. Flower is particularly spammy because it depends on a connection to a different
service, namely celery.

By executing `docker ps -a` you should see something similar to below, and note under the __STATUS__ category, all containers are currently running, which signifies success.