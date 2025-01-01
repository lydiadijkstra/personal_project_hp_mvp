# Harmonic Parent API  
The Harmonic Parent API is designed to help parents navigate challenging situations with their children by providing AI-generated daily tips. This tool offers structured guidance for managing common parenting stressors, such as hitting, yelling, or managing time effectively.

<p>
    If you like the Harmonic Parent API, please give me a star:
</p>
<a href="https://github.com/lydiadijkstra/personal_project_hp_mvp">
    Klick here the give a star, clone or fork the repository
</a>


## Features:

## Features  
- Daily AI-generated parenting tips for common challenges  
- Secure user authentication using JWT  
- Seamless database migration with Alembic


## Table of Contents  
- [Features](#features)  
- [Setup](#setup)  
- [API Endpoints](#api-endpoints)  
- [Project Structure](#project-structure)  
- [Tech Stack](#tech-stack)  
- [Contributing](#contributing)  



## Structured Tree

```sh
├── alembic               # Manages database migrations
├── app
│   ├── api
│   │   ├── endpoints     # Contains modules for each feature (user, children, tips).
│   │   │   └── user
│   │   │   └── children
│   │   │   └── tips
│   │   └── routers       # Contains FastAPI routers, where each router corresponds to a feature.
│   ├── core              # Contains core functionality like database management, dependencies, etc.
│   ├── main.py           # Initializes the FastAPI app and brings together various components.
│   ├── models            # Contains modules defining database models for users, products, payments, etc.
│   ├── schemas           # Pydantic model for data validation
```


## Setup  
Follow these steps to set up the project locally:  

1. Clone the repository:  

```sh
   ```bash  
$ git clone https://github.com/username/harmonic-parent.git
$ cd personal_project_mvp 
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv  
$ source venv/bin/activate  
```

Then install the dependencies:

```sh
# for fixed version
(venv)$ pip install -r requirements.txt
```

Run Database Migrations:

```sh
(venv)$ alembic upgrade head
```

Start the server:

```sh
(venv)$ uvicorn app.main:app --reload
```


## Major Endpoints

| METHOD   | ROUTE              | FUNCTIONALITY                  | Fields                                                                                |
| -------- | ------------------ | ------------------------------ | ------------------------------------------------------------------------------------- |
| _POST_   | `/login`           | _Login user_                   | _**email**, **password**_                                                             |
| _POST_   | `/users/`          | _Create new user_              | _**email**, **password**, name, username, location_                                      |
| _GET_    | `/users/`          | _Get all users list_           | _email, hashed_password, name, username, location, role, is_active, created_at, id_ |
| _PATCH_  | `/users/{user_id}` | _Update the user partially_    | _email, password, name, username, location, role_                                                    |
| _DELETE_ | `/users/{user_id}` | _Delete the user_              | _None_                                                                                |
| _POST_   | `/children/`       | _Create new child_             | _**name**, **issue**, birth date_                                      |
| _POST_   | `/tips/`           | _Create new tip for issue_     | _**name**, **issue**, birth date_                                      |
| _GET_    | `/`                | FastAPI Docs (a.k.a Swagger)_  | _None_                                                                                |
| _GET_    | `/admin`           | _Admin Dashboard_              | _None_                                                                                |

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


<p>
    >> This API was created with the FastAPI Starter Kit from Mahmud Jewel. <<
</p>
<a href="https://github.com/MahmudJewel/fastapi-starter-boilerplate">
    Klick here to create your own API with Mehmud's Starter Kit
</a>
