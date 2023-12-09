AssistantAI


### Description: 
Chatbot powered by gpt-3.5-turbo answers questions related marketing or traveling.


## Installation:

Clone the project and then go to the root directory and create .env file like in .env.example 
(You might want to change the credentials). Then you can install app in tho ways:


### 1. Installation with docker:

Go to the root dir and build the image:

```commandline
docker build -t assistants .
```
then run container:
```commandline
docker run -p 127.0.0.1:8000:8000 -v .:/app assistants
```

### 1. Manual installation:

First install the dependencies from the pyproject.toml file (you will need poetry, so if you don't have it, install 
it using the 'pip install poetry' command), and run:


```commandline
poetry install
```

Then run command:

```commandline
uvicorn app.main:app
```

## Usage:

To ask question you have to send post request to http://127.0.0.1:8000/api/v1/query/

with request body parameter {"query": "your question"}

Swagger documentation is available on http://127.0.0.1:8000/docs#/