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
* Automatic HTML test reports
* Logging
* Multi-browser execution

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **JSON test data**
* **Pytest-HTML**

## 📋 Test Coverage

The project covers the following scenarios:

* Login with valid credentials
* Login with invalid credentials
* Login with empty credentials
* Appointment booking
* Appointment history verification
* Logout from menu and profile
* Appointment form validation

Detailed test cases for the automated scenarios are available in the [`testCases`](./testCases) folder.

## ✨ Framework Features

* Page Object Model for maintainable and reusable test code
* Explicit waits for synchronization
* External JSON test data
* Pytest fixtures and parameterization
* Multi-browser execution
* Automatic screenshots on test failure
* Automatic timestamped HTML test reports
* Logging
* Reusable common Selenium methods through `BaseClass`

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

## 🚀 Setup

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd cura-healthcare-automation
```

Install the required Python packages:

```bash
pip install selenium pytest pytest-html
```

## ▶️ Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests using a specific browser:

```bash
pytest --browser=chrome
```

```bash
pytest --browser=firefox
```

```bash
pytest --browser=edge
```

## 📊 HTML Test Reports

HTML test reports are generated **automatically** when the test suite is executed.

Run:

```bash
pytest
```

A timestamped HTML report is automatically generated in the `reports` folder:

```text
reports/report_<timestamp>.html
```

For example:

```text
reports/report_2026-09-16_20-15-32.html
```

The report includes the test execution results and failure screenshots when applicable.

## 📸 Failure Screenshots

Screenshots are automatically captured when a test fails.

The screenshots are:

* Saved in the `screenshots` folder
* Embedded in the generated HTML test report

This provides visual evidence of the application state at the time of failure and helps with troubleshooting.

## 🧪 Test Data

Test data is maintained separately in the:

```text
testData/
```

JSON files are used to store test data separately from the test logic, making the tests easier to maintain and update.

## 🌐 Application Under Test

**CURA Healthcare Service**

https://katalon-demo-cura.herokuapp.com/

## 🔧 Browser Support

The framework supports:

* Chrome
* Firefox
* Edge

Browser selection can be controlled through the Pytest command-line option:

```bash
pytest --browser=<browser>
```

Example:

```bash
pytest --browser=chrome
```
* Logging
* Reusable Selenium utilities
