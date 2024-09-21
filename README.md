# The FoodFit Backend

The FoodFit is a health and fitness marketplace platform developed to provide users with personalized recommendations for meals and fitness activities based on their health goals, dietary restrictions, and preferences.

This repository contains the backend code for the platform. This document will guide you through setting up the backend on your local machine.

## Table of Contents

-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Running the Application](#running-the-application)
-   [Testing](#testing)
-   [Payment Integration](#payment-integration)
-   [API Documentation](#api-documentation)
-   [Contributing](#contributing)
-   [License](#license)

## Installation
To set up the project, follow these steps:

1.  Clone the repository:
```
git clone <repository-url>
cd foodfit-backend
```
2.  Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3.  Install the required dependencies:
```
pip install -r requirements/base.txt
```
4. Rename the `.env.copy` file to `.env` and configure it with your environment-specific variables:
```
mv .env.copy .env
```
5. Update the `.env` file with the following details:
-   `DB_NAME`
-   `DB_USER`
-   `DB_PASSWORD`
-   `DB_HOST`
-   `DB_PORT`
-   Other required credentials
## Configuration

Ensure that the database is set up according to your local or production environment needs, and apply migrations:
```
python manage.py migrate
```
## Running the Application

To run the application locally, use the following command:
```
python manage.py runserver
```
You should now be able to access the app at `http://127.0.0.1:8000/`.
## Payment Integration

If you are testing payment integration, you will need to obtain a token from [Payze](https://payze.io/) and fill in the following fields in your `.env` file:

-   `PAYZE_AUTH_TOKEN`
-   `PAYZE_SUCCESS_URL`
-    `PAYZE_ERROR_URL`
-   `PAYZE_WEBHOOK_URL`

## API Documentation

The API documentation is available via Swagger. You can access it at the following link:

-   [Swagger API Documentation](https://satyr-helped-intensely.ngrok-free.app/swagger/)

## Contributing

We welcome contributions to the project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bugfix.
3.  Submit a pull request once your changes are tested and documented.
