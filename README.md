# Project Management System

This is a comprehensive project management system built with Django, designed to facilitate the tracking and management of projects, tasks, and team collaboration. The application supports essential project management functionalities, from project and task creation to activity logging and user notifications.

## Features
- **Project and Task Management**: Users can create projects, assign tasks with priorities and due dates, and track completion status.
- **Role-Based Access**: Custom permissions for project owners, members, and task assignees.
- **Nested Comments**: Supports threaded comments to facilitate team communication on tasks.
- **Activity Logging**: Automatically logs actions (like project/task creation, updates, and deletions) for better tracking.
- **Real-Time Notifications**: Sends email notifications to members when projects or tasks are updated.
- **Search & Filtering**: Powerful search and filter capabilities for tasks, including by status, due date, and assigned user.
- **RESTful API**: Built with Django REST Framework, enabling integration with other applications.
- **Pagination**: Supports pagination for improved data handling and user experience.
- **User Registration and Authentication**: Secured user authentication, including JWT support for API requests.

## Technology Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (or SQLite for development)
- **Real-Time Notifications**: Email (Django's email backend)
- **Search & Filtering**: Django Filter backend for precise querying
- **Pagination**: Page-based navigation with customizable page size limits

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alirezaniko/ProjectManagementSystem.git
   cd ProjectManagementSystem

   #Set up a virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
Configure the database: Set up your PostgreSQL database and add your credentials to settings.py.

2. **Run migrations and start the server**:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Usage
Access the application at http://127.0.0.1:8000/
The Django admin interface is available at http://127.0.0.1:8000/admin/ for managing projects, tasks, and user accounts.

Endpoint	Method	Description
- **/api/projects/	GET	List all projects
- **/api/projects/	POST	Create a new project
- **/api/projects/<id>/	PUT	Update a project
- **/api/projects/<id>/	DELETE	Delete a project
- **/api/tasks/	GET	List all tasks
- **/api/tasks/	POST	Create a new task
- **/api/tasks/<id>/	PUT	Update a task
- **/api/tasks/<id>/	DELETE	Delete a task
- **/api/activity_logs/	GET	View activity logs (read-only)
