# Gas Utility Service Management

A Django-based web application that allows customers to submit service requests, track their status, and view account information. Customer support representatives can manage service requests and assist users.

## Features

- **User Registration & Authentication**: Users can register, log in, and log out.
- **Service Requests**: Customers can submit service requests with details and attachments.
- **Request Tracking**: Users can track the status of their service requests.
- **Admin Dashboard**: Support staff can manage and resolve customer service requests.
- **Basic Styling**: Integrated static files for a simple, clean UI.

## Project Directory Structure

```
gas_utility/
├── gas_utility/         # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── service/             # Main application
│   ├── migrations/
│   ├── templates/
│   │   ├── service/
│   │   │   ├── register.html
│   │   │   ├── login.html
│   │   │   ├── submit_request.html
│   │   │   ├── request_list.html
│   │   │   ├── request_detail.html
│   │   │   ├── manage_requests.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── tests.py
├── static/              # Global static files
│   ├── css/
│   │   ├── style.css
├── media/               # Created when attachments are added
├── manage.py            # Django management script
└── README.md            # Project documentation
```

## Installation & Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/gas-utility-service.git
   cd gas-utility-service
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**:
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

7. **Access the application**:
   - Open `http://127.0.0.1:8000/` in your browser.
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

- **Customer Actions**:
  - Register and log in.
  - Submit a service request with details and attachments.
  - Track the status of submitted requests.

- **Admin/Support Staff Actions**:
  - View and manage all service requests.
  - Update the status of requests.
  - Provide support to customers.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Contact

For any questions or issues, feel free to reach out or open a GitHub issue.

