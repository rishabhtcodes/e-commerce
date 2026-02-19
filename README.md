# MARS E-Commerce App

MARS is a premium, production-ready E-Commerce platform built with Django, PostgreSQL, and Tailwind CSS. It features a sleek glassmorphism design, advanced catalog management, and a robust cart/order system.

## 🚀 Key Features

*   **Premium UI**: Custom Glassmorphism aesthetic with micro-animations and fluid layouts.
*   **Authentication**: Secure login/signup system with email verification support.
*   **Advanced Catalog**: Slug-based URL structure, category management, and dynamic product sorting.
*   **Interactive Cart**: Service-layer powered cart logic with real-time stock validation.
*   **API Ready**: Integrated Django REST Framework with JWT authentication.
*   **Seeding System**: Custom scripts to populate the store with high-quality sample data and real product photography.

## 🛠️ Tech Stack

*   **Backend**: Python 3.11+, Django 5.2 (LTS)
*   **Database**: PostgreSQL (Dockerized) / SQLite (Fallback)
*   **Frontend**: Tailwind CSS, Vanilla JS
*   **Infrastructure**: Docker, Docker Compose, GitHub Actions
*   **Auth**: SimpleJWT (REST), Django Auth (Web)

## 📦 Prerequisites

*   Python 3.11+
*   PostgreSQL (optional, default is SQLite for quick setup)
*   Docker & Docker Compose (for containerized deployment)

## 🚥 Installation & Setup

1.  **Clone the project**:
    ```bash
    git clone <repository-url>
    cd E-commerce
    ```

2.  **Create and activate virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    Create a `.env` file in the root directory (refer to `.env.example` if available).

5.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

6.  **Seed Sample Data**:
    ```bash
    python seed_products.py
    python update_product_images.py
    ```

7.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```

## 🐳 Docker Deployment

To run the entire stack (Django, Gunicorn, PostgreSQL) in containers:

```bash
docker-compose up --build
```

## 📂 Media & Static

*   **Static Files**: Located in `static/`. Includes `css/style.css` and `images/logo.png`.
*   **Media Files**: Located in `media/products/`. Contains user-uploaded and seeded product photography.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
