# Phone-Email Authentication

This Django project is designed to handle user authentication using either email or phone number. It utilizes Django Allauth for email authentication and Twilio for SMS verification. We'll set up the project using Docker for easy deployment and development.

## Prerequisites

- Docker installed on your machine. You can download it from [Docker's official website](https://www.docker.com/get-started).

## Installation
Clone this repository and create a .env file with the .env.example as an example. Then you can start the project using Docker or manually using virtual environment.

### Using Docker:
```bash
docker-compose up
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Mannually:

**Create a Python virtual environment and activate it.**

   ```bash
   python -m venv env
   source env/bin/activate  # On macOS and Linux
   .\env\Scripts\activate   # On Windows
   ```

**Install the required packages using pip.**

   ```bash
   pip install -r requirements.txt
   ```

**Run migrations to set up the database tables and create a superuser.**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

**Run the development server.**

   ```bash
   python manage.py runserver
   ```

**Access the Django Admin interface.**

   Open a web browser and navigate to [http://localhost:8000/admin](http://localhost:8000/admin).

## Usage

Once the containers are up and running, you can access the Django Admin interface by navigating to `http://127.0.0.1:8000/admin/`. Log in with the superuser account created in step 5.

Here are the API endpoints provided:

- `POST /api/user/login/`: Login with email or phone number.
- `POST /api/user/register/`: Register a new user with email or phone number.
- `POST /api/user/send-sms/`: Send an SMS verification code for phone number verification.
- `POST /api/user/verify-phone/`: Verify phone number using the verification code.
- `GET /user/login/google/`: Login with Google (OAuth).
- `POST /password/reset/`: Reset the password using email.
- `POST /password/change/`: Change the password.
- `POST /logout/`: Logout the user.
- `POST /resend-email/`: Resend email verification.
- `GET /account-email-verification-sent/`: Email verification sent.

For SMS verification, Twilio integration is used. When registering with a phone number, a verification code will be sent via SMS. The user will need to provide this code to complete registration.

## Dependencies

- Django
- Django Rest Framework
- Django Allauth
- Twilio
