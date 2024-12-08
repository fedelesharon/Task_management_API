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

## API Endpoints

| Endpoint                | Method | Description                                   |
|-------------------------|--------|-----------------------------------------------|
| `/api/register/`        | POST   | Register a new user.                         |
| `/api/login/`           | POST   | User login to obtain authentication token.   |
| `/api/projects/`        | GET    | List all projects.                           |
| `/api/projects/`        | POST   | Create a new project.                        |
| `/api/projects/<id>/`   | GET    | Retrieve a specific project by ID.           |
| `/api/projects/<id>/`   | PUT    | Update a project by ID.                      |
| `/api/projects/<id>/`   | DELETE | Delete a project by ID.                      |
| `/api/tasks/`           | GET    | List all tasks.                              |
| `/api/tasks/`           | POST   | Create a new task.                           |
| `/api/tasks/<id>/`      | GET    | Retrieve a specific task by ID.              |
| `/api/tasks/<id>/`      | PUT    | Update a task by ID.                         |
| `/api/tasks/<id>/`      | DELETE | Delete a task by ID.                         |
| `/api/comments/`        | POST   | Add a comment to a task.                     |

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
   git clone https://github.com/<your-username>/task_management_api.git
   cd task_management_api
