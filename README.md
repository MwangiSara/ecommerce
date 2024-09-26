# Description
- a Django Rest Framework (DRF) project for managing customers and orders. The project is designed for simple understanding and extension, with an emphasis on creating RESTFUL APIs, Implementation of data structures, Implementation authentication and authorization via OpenID Connect, writing automated tests at all levels (unit, integration, and acceptance), and integrating CI/CD.
## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Sections](#sections)
- [Screenshots](#screenshots)
- [API Endpoints](#api-endpoints)
- [Unit Testing](#unit-testing)
  - [Running Tests](#running-tests)
  - [Writing Tests](#writing-tests)
- [Coverage](#coverage)
  - [Measuring Coverage](#measuring-coverage)
  - [Improving Coverage](#improving-coverage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
- A simple Django project that inputs/uploads customers and orders using REST API. Requires users to login or signup using their Google accounts (with the help of Openid Connect). Africastalking sms gateway is implemented to add sms functionality.
## Features

- User authentication with OpenID Connect
- Customer management
- Order processing and management
- Responsive design
- Admin panel for managing users, products, and orders

## Technologies Used

- Django
- Djngorestframework
- MySQL
- mozilla-django-oidc
- HTML, CSS, JavaScript
- Bootstrap
- FontAwesome
- Africastalking
- coverage
- Docker
## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- MySQL
- djangorestframework
- mozilla-django-oidc
- python-dotenv
- mysqlclient
- africastalking
- coverage

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/super_store.git```
2. Install Dependencies
``` pip install -r requirements.txt ```
3. Run the Project
```python manage.py migrate```
```python manage.py runserver```
## API Endpoints
- GET [api/order](http://127.0.0.1:8000/order/) - List all orders
- POST [api/order](http://127.0.0.1:8000/order/)- Create a new orders
- GET [api/customer](http://127.0.0.1:8000/customer/) - List all customers
- POST [api/customer](http://127.0.0.1:8000/customer/)- Create a new customers
## Unit Testing
Here are some tests for this project and the steps
### Running test
run your test using ```python manage.py test```
### Write the test
the tests are in test.py
Use Django ```TestCase``` module to create your own tests
## Coverage
To identify which parts of the code are not tested, thereby revealing untested areas that could potentially harbor bugs, use coverage software
### Measuring Coverage
- Install coverage ```pip install coverage```
- run test using coverage ```coverage run manage.py test```
- get report ```coverage report``
- Generate report in HTML ```coverage html```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features. Here are the Steps
  1. Fork the repository
  2. Create a new branch (git checkout -b feature-name)
  3. Make your changes
  4. Commit your changes (git commit -m 'Add new feature')
  5. Push to the branch (git push origin feature-name)
  6. Open a pull request
## License
This project is licensed under the MIT License.
## Contact
If you have any questions, feel free to reach out:
  - Name: Sarah Mwangi
  - Email: mwangisarah113@gmail.com
  - GitHub: Mwangisara
