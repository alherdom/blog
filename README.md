# Django Blog

#### Blog application built with Django framework.
#### Author: Alejandro Hernández Domínguez

## Project

<div align=center;">
    <img src="alejandrosblog.png" alt="Error">
</div>

## Run locally

### Previous steps to run the application locally:

**1. Clone the repo:**

```
git clone https://github.com/alherdom/django_blog.git
```

**2. Create an enviorment in the project root:**

```
python -m venv .venv --prompt blog
```

**3. Activate the environment:**

```
source .venv/bin/activate
```

**4. Install dependencies:**

```
pip install -r requirements.txt
```

**5. Create a ".env" for environment vars:**

```
touch .env
```

### Steps to run the application:

It is recommended to use the "justfile" for a smoother execution.

**1. Running the server locally:**

```
python manage.py runserver
```

or

```
just runserver
```

**2. Starting development server at:**

```
http://127.0.0.1:8000/blog/
``` 

**3. Quit the server with:**

```
ctrl + c
```
