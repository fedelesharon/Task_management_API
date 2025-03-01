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
   
    
 
### Key Points:

1. **Features** section outlines what the API will do, such as user management, task management, etc.
2. **Tools and Libraries** outlines the frameworks and technologies being used.
3. **Installation and Setup** provides step-by-step instructions on how to get the project up and running locally.
4. **API Endpoints** section details all the major endpoints, including request and response examples for each.
5. **Evidence of Functionality** indicates where to find evidence of successful API usage.

This `README.md` file is a comprehensive guide for your project and can be placed directly in your GitHub repository for clarity.

### Endpoints
GET /tasks: Retrieve a list of tasks.

POST /tasks: Create a new task.

GET /tasks/{ taskId}: Retrieve details of a specific task.

PATCH /tasks/{taskId}: Update an existing task.

DELETE /tasks/{taskId}: Delete a specific task.

GET /lists: Retrieve a list of task lists.

POST /lists: Create a new task list.

GET /lists/{listId}: Retrieve details of a specific task list.

PATCH /lists/{listId}: Update an existing task list.

DELETE /lists/{listId}: Delete a specific task list.

GET /tags: Retrieve a list of tags.

POST /tags: Create a new tag.

GET /tags/{tagId}: Retrieve details of a specific tag.

PATCH /tags/{tagId}: Update an existing tag.

DELETE /tags/{tagId}: Delete a specific tag.

GET /subtasks: Retrieve a list of subtasks.

POST /subtasks: Create a new subtask.

GET /subtasks/{subtaskId}: Retrieve details of a specific subtask.

PATCH /subtasks/{subtaskId}: Update an existing subtask.

DELETE /subtasks/{subtaskId}: Delete a specific subtask.   