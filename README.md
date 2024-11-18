# FUTAMSA Web Application

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

FUTAMSA (Federal University of Technology Akure Medical Students Association) is an association for medical students. This web application serves as a platform to manage and share information related to events, resources, and member activities.

## Features

- User Registration and Authentication
- Profile Management
- Event Creation, Management, and Display
- Resource Sharing
- Google Maps Integration for Event Locations
- Email Notifications for Event Reminders
- Image Upload and Storage with Cloudinary

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (development), PostgreSQL (production)
- **APIs**: Google Maps API, SendGrid API, Cloudinary API
- **Version Control**: Git and GitHub

## Installation

### Prerequisites

- Python 3.8+
- Node.js (for frontend dependencies)
- Git

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/futamsa-web-app.git
    cd futamsa-web-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install frontend dependencies:

    ```bash
    cd frontend
    npm install
    cd ..
    ```

5. Set up environment variables. Create a `.env` file in the root directory and add the following:

    ```bash
    FLASK_APP=app
    FLASK_ENV=development
    DATABASE_URL=sqlite:///dev.db  # For development
    SECRET_KEY=your_secret_key
    SENDGRID_API_KEY=your_sendgrid_api_key
    CLOUDINARY_URL=your_cloudinary_url
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```

6. Run database migrations:

    ```bash
    flask db upgrade
    ```

7. Start the development server:

    ```bash
    flask run
    ```

8. Open the application in your browser at `http://127.0.0.1:5000`.

## Usage

### Running Tests

To run tests, use the following command:

```bash
pytest

