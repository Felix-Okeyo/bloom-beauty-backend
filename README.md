Bloom Beauty Management System API

The Bloom Beauty Management System API is a RESTful web service designed to manage beauty products, brands, user profiles, and invoices. It allows you to perform various operations related to your beauty product business.
Table of Contents

    Getting Started
        Prerequisites
        Installation
    API Endpoints
        Home
        User Registration
        User Authentication
        User Profile Management
        Product Management
        Brand Management
        Invoice Management
        Category Management
        Client Management
    Usage Examples
    License

Getting Started
Prerequisites

Before running the Bloom Beauty Management System API, you need to have the following installed:

    Python 3.x
    Flask
    Flask extensions (Flask-RESTful, Flask-JWT-Extended, Flask-CORS)
    SQLite (for the default database)
    Any required Python packages specified in your requirements.txt

Installation

    Clone the repository:

    bash

git clone git@github.com:Felix-Okeyo/bloom-beauty-frontend.git

Navigate to the project directory:

bash

cd bloom-beauty-backend

Install the required packages using pip:

bash

pip install -r requirements.txt

Run the API:

bash

    python app.py

The API should now be running on http://localhost:5555.
API Endpoints
Home

    URL: /
    Description: Retrieve a welcome message.
    HTTP Method: GET
    Authentication: Not required

User Registration

    URL: /register
    Description: Register a new user.
    HTTP Method: POST
    Authentication: Not required

User Authentication

    URL: /login
    Description: Authenticate a user and obtain an access token.
    HTTP Method: POST
    Authentication: Not required

User Profile Management

    URL: /profile/{user_id}
    Description: Get, update, or delete user profiles.
    HTTP Method: GET, PUT, DELETE
    Authentication: Required

Product Management

    URL: /products

    Description: Get a list of products or add new products.

    HTTP Method: GET, POST

    Authentication: Required for POST

    URL: /products/{product_id}

    Description: Get, update, or delete a product.

    HTTP Method: GET, PATCH, DELETE

    Authentication: Required for POST and DELETE

Brand Management

    URL: /brands

    Description: Get a list of brands or add new brands.

    HTTP Method: GET, POST

    Authentication: Required for POST

    URL: /brands/{brand_id}

    Description: Get, update, or delete a brand.

    HTTP Method: GET, PATCH, DELETE

    Authentication: Required for POST and DELETE

Invoice Management

    URL: /invoices

    Description: Get a list of invoices.

    HTTP Method: GET

    Authentication: Required

    URL: /invoices/{invoice_id}

    Description: Get details of a specific invoice.

    HTTP Method: GET

    Authentication: Required

Category Management

    URL: /categories
    Description: Get a list of product categories.
    HTTP Method: GET
    Authentication: Not required

Client Management

    URL: /clients
    Description: Get a list of clients (users).
    HTTP Method: GET
    Authentication: Required

Usage Examples

For usage examples and API request samples, please refer to the API documentation.
License

This project is licensed under the MIT License - see the LICENSE file for details.

