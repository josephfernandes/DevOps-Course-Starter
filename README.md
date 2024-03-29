# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Before Running the app

The set up of this to_do app has been designed for Trello. Set up the .env file and place the information accordingly to your Trello account and then include it in the gitignore file so your secrets do not get commited.

SECRET_KEY=secret-key # leave this as it is

API_KEY = 'abc'
API_TOKEN = 'def'
BOARD = 'ghi'
TO_DO= 'klm'
DOING= 'nop'
Done=  'qrs'
```

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

Ansible: There are Ansibles files in the Ansible folder and you can run the command:

``` 
ansible-playbook my-ansible-playbook.yml -i inventory.txt

```
## Docker Module 5
```
Command in the terminal to build the image
docker build --target development --tag todo-app:dev .    

(Development Image)
 docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
or    docker build --target development --tag todo-app:dev .

(Production Image )
docker build --target production --tag todo-app:prod . 
docker run --env-file ./.env -p 5000:5000 todo-app:prod
or  docker build --target production t --tag todo-app:dev .

(Test Image )
docker build --target test --tag todo-app:test . 
docker run todo-app:test

[comment for me: ports on dockercompose file, the right one is for local machine and left is of the container. in order for the app to run Expose port should be same as the right. eg 80:4000  left for locahost and to run in the browser it should be localhost:80]

(Docker-Compose Commands)

docker-compose up --build 


docker-compose up todo-dev
docker-compose up todo-prod
docker-compose up todo-test

misc:CMD ["poetry", "run", "flask","run","--host=0.0.0.0"] (to run on flask only )
poetry add gunicorn        (to add gunicorn)                            
```

az cosmosdb keys list -n jo-fernandes -g
KPMG21_JosephFernandes_ProjectExercise --type connection-strings

az appservice plan create --resource-group KPMG21_JosephFernandes_ProjectExercise -n jo-plan --sku B1 --is-linux

az webapp create --resource-group  --KPMG21_JosephFernandes_ProjectExercise --plan jo-plan --name jo-todo-app --deployment-container-image-name josephfernandes14/todoapp:latest

new environment variables 

CONNECTION_STRING=
DATABASE=
COLLECTION=
PRIMARYKEY=

