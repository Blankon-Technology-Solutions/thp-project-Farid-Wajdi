# My Todo App

This is a Django-based todo app that allows users to manage their tasks and todos. It provides a RESTful API for creating, updating, and deleting tasks. The app also supports user authentication with Google OAuth.

## Project Structure

The project has the following file structure:

```
docker-compose.yml
Dockerfile
manage.py
README.md
requirements.txt
set_env.sh
todo_list/
	__init__.py
	asgi.py
	consumers.py
	middleware.py
	migrations/
		__init__.py
		0001_initial.py
	models/
		__init__.py
		todo.py
		user.py
	routing.py
	serializers/
		__init__.py
	settings.py
	urls/
		__init__.py
	views/
		__init__.py
		...
	wsgi.py
```

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

```sh
git clone git@github.com:Blankon-Technology-Solutions/thp-project-Farid-Wajdi.git
```

2. Install the requirements:

```sh
pip install -r requirements.txt
```

3. Run the migrations:

```sh
python manage.py migrate
```

4. Start the server:

```sh
daphne todo_list.asgi:application -b 0.0.0.0 --port 8000 
```
Now, you can hit `http://localhost:8000` in your web browser to see the app in action.

Note: this will not run properly on WSL (Windows Subsystem for Linux). User Docker compose instead.
## Running with Docker

You can also run this app with Docker using the provided Dockerfile and docker-compose.yml file. To do this, run the following command:

```sh
docker-compose up
```

This will build the Docker image and start the app and a PostgreSQL database in separate Docker containers. The app will be available at `http://localhost:8000`.

## Curl Samples
Register a user
```bash
curl --request POST \
  --url http://localhost:8000/dj-rest-auth/registration/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"username":"test1",
	"password1": "mytestpassaccount",
	"password2": "mytestpassaccount",
	"email": "test1@gmail.com"
}'
```

Login a user
```bash
curl --request POST \
  --url http://localhost:8000/dj-rest-auth/login/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"username":"test1",
	"password": "mytestpassaccount"
}'
```


List Todo
```bash
curl --request POST \
  --url http://localhost:8000/dj-rest-auth/login/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"username":"test1",
	"password": "mytestpassaccount"
}'
```

Create Todo
```bash
curl --request POST \
  --url http://localhost:8000/todos/ \
  --header 'Authorization: Token {token}' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"title": "title-test",
	"description": "description"
}'
```

Get Todo
```bash
curl --request GET \
  --url http://localhost:8000/todos/36aa8869-a9d3-4549-8d07-d87f4c500260/ \
  --header 'Authorization: Token {token}' \
  --header 'User-Agent: insomnia/8.6.1'
```


Update Todo
```bash
curl --request PUT \
  --url http://localhost:8000/todos/4dc5f7d1-6176-45d3-bb8b-cdb6863bff3a/ \
  --header 'Authorization: Token {token}' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"title": "title-test-2",
	"description": "description"
}'
```

Delete Todo
```bash
curl --request DELETE \
  --url http://localhost:8000/todos/4dc5f7d1-6176-45d3-bb8b-cdb6863bff3a/ \
  --header 'Authorization: Token {token}' \
  --header 'User-Agent: insomnia/8.6.1' \
```

Get Google Login Creds
```bash
curl --request POST \
  --url 'https://accounts.google.com/o/oauth2/v2/auth?client_id={google client id}&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Fcallback%2F&prompt=consent&response_type=code&scope=openid%20email%20profile&access_type=offline' \
  --header 'User-Agent: insomnia/8.6.1' \
```

Google Login Creds
```bash
curl --request POST \
  --url http://localhost:8000/dj-rest-auth/google/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
	"code": "{code from redirect url after login google}"
}'
```

Websocket Connection
```bash
# Using websocat (https://github.com/vi/websocat?tab=readme-ov-file#installation)
websocat ws://localhost:8000/ws/todo/ -H "Authorization: Token {token}"
```
Can also use Insomnia or Postman with additional Header "Authorization: Token {token}"
