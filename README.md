# CURA Healthcare Automation

A Selenium WebDriver automation project for testing the **CURA Healthcare Service** web application using Python, Pytest, and the Page Object Model (POM).

## 🧪 Project Overview

This project automates key user workflows of the CURA Healthcare Service application, including login, appointment booking, appointment history, logout, and form validation.

The framework is designed with maintainability and reusability in mind using:

* Page Object Model (POM)
* Pytest fixtures
* Explicit waits
* External JSON test data
* Parameterized tests
* Screenshot capture on test failure
* HTML test reports
* Logging
* Multi-browser execution

## 🛠️ Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* JSON test data
* Pytest-HTML

## 📋 Test Coverage

* Login with valid, invalid, and empty credentials
* Appointment booking
* Appointment history verification
* Logout from menu and profile
* Appointment form validation
* Multi-browser execution: Chrome, Firefox, Edge
* Failure screenshot capture
* HTML test reporting
* Logging

Detailed test cases for the automated scenarios are available in the [`testCases`](./testCases) folder.

## 📁 Project Structure

```text
CuraHealthCareTests/
├── pages/
├── testData/
├── testCases/
├── tests/
├── utils/
├── conftest.py
├── .gitignore
└── README.md
```

## ▶️ Run Tests

Install dependencies:

```bash
pip install selenium pytest pytest-html
```

Run all tests:

```bash
pytest
```

Run with a specific browser:

```bash
pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge
```

## 🌐 Application

**CURA Healthcare Service**

https://katalon-demo-cura.herokuapp.com/

## 📌 Framework Highlights

* Page Object Model for maintainable test code
* Explicit waits for synchronization
* External JSON test data
* Pytest fixtures and parameterization
* Automatic screenshots on test failure
* HTML test reports
