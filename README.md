# Invoice Management System

## Overview

This project is an invoice management system using Django and Django REST framework. It provides RESTful endpoints to manage invoices, including listing, and uploading invoices via CSV files.

## Requirements

- Python 3.x
- Django 4.x
- Django REST framework 3.x
- Celery


## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/micky225/Client_Invoice_Management.git
    Navigate to the projects root directory
    ```

2. Create a virtual environment (example .venv) and install dependencies:
    ```sh
    python -m venv .venv

    - On Windows:
    .venv\Scripts\activate
   
   - On macOS and Linux:
    source .venv/bin/activate

    pip install -r requirements.txt
    ```

3. Configure Celery with Redis:
    ```sh
    # In settings.py
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    ```

4. Apply database migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Start Celery worker:
    ```sh
    celery -A setup worker --loglevel=info
    ```


## Running Tests

```sh
python manage.py test
```


### 4. Ensure All REST Endpoints Respond Within 100ms

To ensure all REST endpoints respond within 100ms, consider the following:

1. **Database Optimization:**
   - Ensure your database queries are optimized.
   - Add appropriate indexes on frequently queried fields.

2. **Efficient Querying:**
   - Use Django's `select_related` and `prefetch_related` to optimize query performance.

3. **Asynchronous Tasks:**
   - Offload long-running tasks to Celery to keep the main thread responsive.

### 5. Running the Application

Follow the instructions in the README to set up, run, and test your application.

### Conclusion

By following these steps, you can ensure all requirements, including performance constraints and proper documentation. This will result in a robust, well-documented, and high-performing application.