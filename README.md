# Project Offers

## Overview

The Project Offers is a web application built with Django that scrapes product information from a website and displays it in a catalog. Users can filter products by free shipping and shipping type, and sort them by price or discount.

## Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd project_offers
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (optional, for accessing the admin site):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the home page to see the product catalog.
- Use the filters and sorting options to customize the product display.
- To scrape new products, visit `http://127.0.0.1:8000/`.

## Project Structure

- `app_offers/`: Contains the main application code.
- `project_offers/`: Contains the project settings and configuration.
- `templates/`: Contains the HTML templates for rendering the web pages.
- `static/`: Contains static files like CSS and JavaScript.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
