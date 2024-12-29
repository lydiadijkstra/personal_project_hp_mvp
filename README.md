# HARMONIC PARENT API

This API was created with the FastAPI Starter Kit from Mahmud Jewel.
<p>
    If you like the Harmonic Parent API, please give me a star:
</p>
<a href="https://github.com/lydiadijkstra/personal_project_hp_mvp">
    Klick here the give a star, clone or fork the repository
</a>


## Features:

- FastAPI project structure tree
- user module
  - id, first name, last name, **email** as username, **password**, role, is_active created_at, updated_at
- admin dashboard => sqladmin
- authentication => JWT
- db migration => alembic
- CORS middleware

## Structured Tree

```sh
├── alembic     # Manages database migrations
├── alembic.ini
├── app
│   ├── api
│   │   ├── endpoints   # Contains modules for each feature (user, children, tips).
│   │   │   ├── __init__.py
│   │   │   └── user
│   │   │       ├── auth.py
│   │   │       ├── functions.py
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   │   └── children
│   │   │       ├── functions.py
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   │   └── tips
│   │   │       ├── functions.py
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   ├── __init__.py
│   │   └── routers     # Contains FastAPI routers, where each router corresponds to a feature.
│   │       ├── api.py
│   │       ├── __init__.py
│   │       ├── children.py
│   │       ├── tips.py
│   │       └── user.py
│   ├── core    # Contains core functionality like database management, dependencies, etc.
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── create_tip_daily.py
│   │   ├── modules.py
│   │   ├── gemini_api_datafetcher.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── main.py     # Initializes the FastAPI app and brings together various components.
│   ├── create_table.py # Pre-Setup for creating a new table in the DB
│   ├── models      # Contains modules defining database models for users, products, payments, etc.
│   │   ├── admin.py
│   │   ├── common.py
│   │   ├── children.py
│   │   ├── tips.py
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas   # Pydantic model for data validation
│   │   ├── __init__.py
│   │   ├── tips.py
│   │   ├── children.py
│   │   └── user.py
│   └── 
├── requirements.txt # Lists project dependencies.
├── README.md
├── docs
│   ├── docs.odt
```

**app/api/endpoints/**: Contains modules for each feature (user, children, tips).

**app/api/routers/**: Contains FastAPI routers, where each router corresponds to a feature.

**app/models/**: Contains modules defining database models for users, children, tips, etc.

**app/core/**: Contains core functionality like database management, dependencies, etc.

**app/schemas/**: Contains the Class Schemas that are used across different features.

**app/main.py**: Initializes the FastAPI app and brings together various components.

**alembic/**: Manages database migrations.

**docs/**: Holds documentation files.

**requirements.txt**: Lists project dependencies.

# Setup

The first thing to do is to clone the repository:

```sh
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ cd fastapi-starter-kit
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
# for fixed version
(venv)$ pip install -r requirements.txt

# or for updated version
(venv)$ pip install -r dev.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

```sh
# db migrations
(venv)$ alembic upgrade head

# start the server
(venv)$ uvicorn app.main:app --reload
```

## User module's API

| SRL | METHOD   | ROUTE              | FUNCTIONALITY                  | Fields                                                                                |
| --- | -------- | ------------------ | ------------------------------ | ------------------------------------------------------------------------------------- |
| _1_ | _POST_   | `/login`           | _Login user_                   | _**email**, **password**_                                                             |
| _2_ | _POST_   | `/refresh/?refresh_token=`           | _Refresh access token_|_None_ 
| _3_ | _POST_   | `/users/`          | _Create new user_              | _**email**, **password**, first name, last name_                                      |
| _4_ | _GET_    | `/users/`          | _Get all users list_           | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _5_ | _GET_    | `/users/me/`       | _Get current user details_     | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _6_ | _GET_    | `/users/{user_id}` | _Get indivisual users details_ | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _7_ | _PATCH_  | `/users/{user_id}` | _Update the user partially_    | _email, password, is_active, role_                                                    |
| _8_ | _DELETE_ | `/users/{user_id}` | _Delete the user_              | _None_                                                                                |
| _9_ | _GET_    | `/`                | _Home page_                    | _None_                                                                                |
| _10_ | _GET_    | `/admin`           | _Admin Dashboard_              | _None_                                                                                |

# Tools

### Back-end

#### Language:

    Python

#### Frameworks:

    FastAPI
    pydantic

#### Other libraries / tools:

    SQLAlchemy
    starlette
    uvicorn
    python-jose
    alembic
    google generative ai
    random

### Happy Coding
