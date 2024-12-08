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
  **Backend Framework**: Django and Django Rest Framework (DRF).
  **Database**: MySQL relational database.
  **Authentication**: Django Rest Framework's token authentication.
  **Version Control**: Git and GitHub.
  **Deployment**: Render or Heroku.
  
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
   
    