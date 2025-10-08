# Flask Learning Project

A comprehensive collection of Flask applications demonstrating various web development concepts and API development techniques.

## Project Overview

This project contains multiple Flask applications that showcase different aspects of web development using the Flask framework. It's designed as a learning resource to understand Flask fundamentals, REST API development, template rendering, and form handling.

## Features

- **Basic Flask Application** (`app.py`) - Simple routes and responses
- **REST API** (`api.py`) - Complete CRUD operations for a TODO list
- **Template Rendering** (`main.py`) - HTML template integration
- **Form Handling** (`getpost.py`) - GET/POST request processing
- **Dynamic URL Routing** (`jinja.py`) - Jinja2 templating with URL parameters
- **HTML Templates** - Form and result page templates

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Flask
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
Flask/
├── app.py           # Basic Flask application with simple routes
├── api.py           # REST API for TODO list management
├── main.py          # Template rendering example
├── getpost.py       # Form handling with GET/POST methods
├── jinja.py         # Dynamic URL routing with Jinja2 templates
├── requirements.txt # Python dependencies
├── sample.json      # Sample data for testing
└── templates/       # HTML templates
    ├── index.html   # Basic index page
    ├── form.html    # Form template
    └── result.html  # Results display template
```

## Usage

### 1. Basic Flask App (`app.py`)

Run the basic Flask application:

```bash
python app.py
```

Visit the following endpoints:
- `http://localhost:5000/` - Welcome message
- `http://localhost:5000/index` - Index page

### 2. TODO API (`api.py`)

Run the REST API server:

```bash
python api.py
```

Available endpoints:
- `GET /` - Welcome message
- `GET /items` - Retrieve all items
- `GET /items/<id>` - Retrieve specific item by ID
- `POST /items` - Create new item (JSON format)
- `PUT /items/<id>` - Update existing item
- `DELETE /item/<id>` - Delete item

**Example POST request:**
```json
{
    "name": "New Task",
    "description": "Task description"
}
```

### 3. Template Rendering (`main.py`)

Run the template application:

```bash
python main.py
```

Endpoints:
- `http://localhost:5000/` - Welcome message
- `http://localhost:5000/index` - Renders HTML template

### 4. Form Handling (`getpost.py`)

Run the form handling application:

```bash
python getpost.py
```

Endpoints:
- `GET /home` - Display form
- `POST /form` - Process form submission

### 5. Dynamic URLs (`jinja.py`)

Run the Jinja2 templating application:

```bash
python jinja.py
```

Endpoints:
- `/success/<score>` - Display follower count
- `/influencer/<count>` - Check influencer status (returns "Passed" if count >= 10,000)

## Technologies Used

- **Flask** - Web framework for Python
- **Jinja2** - Template engine for HTML rendering
- **HTML/CSS** - Frontend markup and styling

## Learning Objectives

This project demonstrates:

- Flask application setup and configuration
- Route definition and URL handling
- HTTP methods (GET, POST, PUT, DELETE)
- JSON API development
- Template rendering with Jinja2
- Form data processing
- Dynamic URL parameter handling
- Basic CRUD operations

## Contributing

This is a learning project. Feel free to experiment with the code and add new features to practice Flask development.

## License

This project is for educational purposes only.
