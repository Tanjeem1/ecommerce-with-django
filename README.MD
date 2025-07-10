# Ecommerce-with-django


## Overview
This is a Django-based e-commerce application utilizing modern web technologies and containerization. It integrates HTMX for dynamic HTML, CSS for styling, Stripe for payment processing, and Docker for container management.

## Features
- Product catalog management
- Shopping cart functionality
- Order processing
- Payment integration with Stripe
- Responsive design with HTML/CSS
- Dynamic updates using HTMX

## Tech Stack
- **Backend**: Django
- **Frontend**: HTMX, HTML, CSS
- **Payments**: Stripe
- **Containerization**: Docker, Docker Compose
- **Database**: SQLite3

## Prerequisites
- Docker
- Docker Compose
- Python 3.x
-stripe account

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Tanjeem1/ecommerce-with-django.git
   cd ecommerce-with-django

## Build and start the Docker containers:bash

docker-compose up --build

Access the host application at http://localhost:8001


## Build and start locally:bash

cd furniture

install requiments.txt file

run manage.py command

Access the dockerize application at http://localhost:8000

## Must need to have a stripe account for testing the transiction


## Project Structurevenv

env/: Virtual environment

furniture/: Main app directory

cart/, core/, media/, order/, product/: App modules

dockerignore: Docker ignore file

db.sqlite3: SQLite database

docker-compose.yml: Docker Compose configuration

Dockerfile: Docker configuration

manage.py: Django management script

requirements.txt: Python dependencies

info.txt: Additional project info



This README provides a basic overview, installation steps, and structure based on the visible files. Let me know if you'd like to expand any section @tanjeemhridoy93@gmail.com