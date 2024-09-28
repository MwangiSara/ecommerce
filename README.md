![APIs](image.png)
# Description
- a Django Rest Framework (DRF) project for managing customers and orders. The project is designed for simple understanding and extension, with an emphasis on creating RESTFUL APIs, Implementation of data structures, Implementation authentication and authorization, writing automated tests at all levels (unit, integration, and acceptance), and integrating CI/CD.
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
- A simple Django project that inputs/uploads customers, products and orders using REST API. Requires users to authenticate themselves using JWT. Africastalking sms gateway is implemented to add sms functionality.
## Features

- User authentication
- Customer management
- product management
- Order processing and management
- Swagger API UI
- Admin panel for managing groups

## Technologies Used

- Django
- Djngorestframework
- Postgresql
- drf-yasg
- JWT
- Africastalking
- coverage
- Terraform
- AWS

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- Postgresql
- djangorestframework
- africastalking
- coverage
- Terraform
- AWS
- JWT

### Installation

1. Clone the repository:
   ```sh
   https://github.com/MwangiSara/ecommerce.git```
2. Install Dependencies
``` pip install -r requirements.txt ```
3. make sure you have postgresql
4. Run the Project
```python manage.py migrate```
```python manage.py runserver```
5. On Your browser enter ```127.0.0.1:8000/developer/docs```
## API Endpoints
- POST [http://127.0.0.1:8000/api/account/create/customer/](http://127.0.0.1:8000/api/account/create/customer/) - register as a customer
- POST [http://127.0.0.1:8000/auth/jwt/create/](http://127.0.0.1:8000/auth/jwt/create/)- Get access token
- POST [http://127.0.0.1:8000/auth/jwt/verify/](http://127.0.0.1:8000/auth/jwt/verify/) - verify access token
- POST [http://127.0.0.1:8000/api/order/products/](http://127.0.0.1:8000/api/order/products/)- Create an Item
- POST [http://127.0.0.1:8000/api/order/orders/](http://127.0.0.1:8000/api/order/orders/)- Create an order
- GET [http://127.0.0.1:8000/api/order/orders/detail](http://127.0.0.1:8000/api/order/orders/detail)- get order details
- GET [http://127.0.0.1:8000/api/order/search/](http://127.0.0.1:8000/api/order/search/)- search order with date
## Database
![database](image-2.png)
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
![coverage](image-1.png)
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
