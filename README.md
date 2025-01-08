# Blood Bank Management System

This repository contains a **Django web application** designed for managing a blood bank. The application streamlines the process of managing donor information, blood inventory, and user requests for blood, providing a user-friendly platform for administrators, donors, and recipients.

---

## 🚀 Features

- **Donor Management**: Register and manage donor information, including contact details and blood type.
- **Blood Inventory Tracking**: Maintain real-time updates on blood stock availability.
- **Request Management**: Enable users to request blood and track the status of their requests.
- **Authentication System**:
  - Role-based access for **Admin**, **Donor**, and **Recipient**.
  - Secure login and registration system.
- **Search and Filter**: Search for blood groups and filter donors by location and blood type.
- **Responsive UI**: A user-friendly and mobile-responsive interface.

---

## 📂 Project Structure

```plaintext
├── blood_bank/          # Main Django project folder
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI application entry point
├── app/                 # Main application folder
│   ├── templates/       # HTML templates for the web app
│   ├── static/          # Static files (CSS, JavaScript, images)
│   ├── views.py         # Application logic
│   ├── models.py        # Database models
│   ├── urls.py          # Application-level URL routing
│   ├── forms.py         # Django forms for user input
│   ├── admin.py         # Admin site configuration
├── db.sqlite3           # SQLite database (default)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── LICENSE              # License information
