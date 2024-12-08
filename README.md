# Task Management API

A Django-based API for managing tasks, projects, and user assignments with role-based access control.

## Features

- **User Management**:  
  - User registration and authentication (JWT or Django authentication).
  - Role-based access control (e.g., Admin, Manager, Member).

- **Project Management**:  
  - Create, update, and delete projects.
  - Assign users to projects.

- **Task Management**:  
  - Create, update, and delete tasks within a project.
  - Set priorities (low, medium, high) and status (to-do, in-progress, completed).
  - Assign tasks to specific users.

- **Comments**:  
  - Add comments to tasks.
  - Track comments by users.

## Tools and Libraries

- **Django**: For building the backend framework and handling database operations, views, and URLs.
- **Django REST Framework (DRF)**: For building the API endpoints, handling serialization, and providing a straightforward way to create APIs.
- **Django ORM**: For database interaction and managing models such as `User`, `Project`, `Task`, and `Comment`.
- **MySQL**: For the database, used to store data related to users, projects, tasks, and comments.
- **JWT or Django Authentication**: For secure user authentication via JWT tokens or Django's built-in authentication system.
- **Postman**: For testing API endpoints and ensuring that they are functioning as expected.
- **Git**: For version control to manage the project and track changes over time.
- **GitHub**: For hosting the project repository and collaboration.
- **Heroku CLI**: For deploying the application to Heroku or other cloud services.
- **Docker (Optional)**: For containerizing the application to ensure consistency across development and production environments.

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- MySQL database (optional, but preferred)
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fedelesharon/Task_management_API.git
   cd task_management_api

2. **Run the server**:
   ```bash
   python manage.py runserver
   
    