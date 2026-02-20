# 🛒 E-Commerce Store

A full-featured e-commerce platform built with **Django**, **PostgreSQL**, and a modern minimal UI.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Auth & Email** | Email-based signup/login with welcome, login, logout & order confirmation emails |
| **Role-Based Access** | Customer and Seller roles with separate login redirects |
| **Product Catalog** | Search, filter by category, sort by price, with pagination |
| **Shopping Cart** | Add, remove, and update item quantities with stock validation |
| **Checkout & Orders** | Full checkout flow with shipping info, order history & detail pages |
| **Account Management** | Profile page, password change, and permanent account deletion |
| **Dark Mode** | Toggle between light and dark themes |
| **Responsive Design** | Mobile-first layout with hamburger menu and horizontal category pills |
| **REST API** | Full API with JWT authentication via Django REST Framework |
| **Security** | CSRF protection, input validation, custom 404/500 error pages |

---

## 🚀 Quick Start

### Prerequisites

- **Python** 3.10+
- **PostgreSQL** installed and running on port 5432

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sunnykumar37/E-Commerce.git
cd E-Commerce

# 2. Create and activate virtual environment
python -m venv env
env\Scripts\Activate        # Windows
# source env/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
copy .env.example .env      # Windows
# cp .env.example .env      # Linux/Mac
# Then edit .env with your actual credentials

# 5. Create the PostgreSQL database
# In psql shell: CREATE DATABASE ecommerce_db;

# 6. Run migrations
python manage.py migrate

# 7. Create a superuser (admin)
python manage.py createsuperuser

# 8. Seed sample products with images
python seed_products.py

# 9. Start the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## ⚙️ Environment Variables

Copy `.env.example` → `.env` and fill in your values:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | `your-random-secret-key` |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated hosts | `localhost,127.0.0.1` |
| `DB_NAME` | PostgreSQL database name | `ecommerce_db` |
| `DB_USER` | PostgreSQL username | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | `your_password` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `EMAIL_HOST_USER` | Gmail address for sending emails | `you@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Gmail App Password ([how to get one](https://myaccount.google.com/apppasswords)) | `xxxx xxxx xxxx xxxx` |

> **Note:** Never commit your `.env` file. It is already in `.gitignore`.

---

## 🗂️ Project Structure

```
E-Commerce/
├── accounts/          # User auth, email service, profile
├── api/               # REST API (DRF + JWT)
├── cart/              # Shopping cart logic
├── ecommerce_app/     # Django settings & root URLs
├── orders/            # Checkout, order history, order detail
├── products/          # Product catalog & categories
├── templates/         # All HTML templates
│   ├── accounts/      # Login, signup, profile, delete account
│   ├── cart/          # Cart detail
│   ├── orders/        # Checkout, history, detail, success
│   └── products/      # Product list, detail, category
├── static/            # CSS, JS, images
├── media/             # User-uploaded product images (gitignored)
├── seed_products.py   # Script to populate sample data
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template
└── .gitignore         # Git exclusions
```

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** Custom CSS with CSS variables, Tailwind CSS (CDN)
- **Auth:** Django built-in + custom email notifications
- **API Auth:** JWT via SimpleJWT
- **Fonts:** Google Fonts (Outfit)

---

## 📧 Email Notifications

The app sends branded emails via Gmail SMTP:

| Event | Subject |
|---|---|
| New signup | `Store \| Welcome to Our Store!` |
| Login | `Store \| New Login to Your Account` |
| Logout | `Store \| You've Been Logged Out` |
| Order placed | `Store \| Order #X Confirmed` |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).