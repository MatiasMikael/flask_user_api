# Flask User API

This is a simple RESTful API built with Flask that allows you to manage users in a SQLite database.

## Features

- **Create a user:** Add a new user with a name and age.
- **Read users:** Retrieve all users or a specific user by ID.
- **Update a user:** Modify an existing user's details.
- **Delete a user:** Remove a user from the database.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flasgger (for Swagger UI)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MatiasMikael/<your-repo-name>.git
   ```

2. Navigate to the project directory:
   ```bash
   cd <your-repo-name>
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage

The API provides the following endpoints:

- **GET /api/users:** Retrieve all users
- **GET /api/users/<user_id>:** Retrieve a user by ID
- **POST /api/users:** Add a new user
- **PUT /api/users/<user_id>:** Update a user by ID
- **DELETE /api/users/<user_id>:** Delete a user by ID

## Swagger Documentation

API documentation is available at [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/).

---

Just replace `<your-repo-name>` with your actual repository name, and it’s ready to use!
