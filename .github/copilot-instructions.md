# GitHub Copilot Instructions for This Project
This document provides guidelines and context for GitHub Copilot to help it generate code that aligns with our project's standards and best practices.

## General Coding Guidelines

 - Language Preference: All new code should primarily be written in Python.
 - Code Style: Adhere strictly to PEP 8 guidelines for all Python code.
 - Indentation: Use 4 spaces for indentation.
 - Quotes: Prefer double quotes (") for all string literals.
 - Docstrings: When generating functions or classes, provide clear and concise docstrings to explain their purpose, arguments, and return values.

## Naming Conventions
To maintain consistency and readability, please follow these naming conventions:

 - Variables: Use snake_case for all variable names (e.g., user_name, total_amount).
 - Functions: Use snake_case for all function names (e.g., get_user_data, calculate_price).
 - Classes: Use PascalCase for all class names (e.g., UserManager, ProductService).
 - Constants: Use UPPER_SNAKE_CASE for all constant names (e.g., MAX_RETRIES, API_KEY).

## Project Context and Technologies
This project is a backend REST API focused on dog training. Copilot should prioritize suggestions related to:

 - Keywords:
    - REST API (creation, endpoints, routing)

 - Frameworks & Libraries:
    - FastAPI: This is the primary web framework used for building the API.
    - SQLModel: We use SQLModel for defining data models and interacting with the database.
    - Pytest: All new code should be accompanied by relevant unit and integration tests using Pytest.
