# Playwright Python Practice Automation

This repository is used for learning and practising Playwright automation with Python using the Page Object Model (POM) design pattern.

## Purpose
- Learn Playwright with Python
- Practise Page Object Model (POM)
- Build and run UI automation tests
- Improve automation skills

## Tech Stack
- Python
- Playwright
- Pytest

## Project Structure
Playwright_Python_Practice_Automation/
├── pages/        # Page Object classes  
├── tests/        # Test cases  
├── utils/        # Helper functions  
├── fixtures/     # Test fixtures  
├── reports/      # Test reports  
├── requirements.txt  
├── pytest.ini  
└── README.md  

## Setup
1. Create virtual environment  
python -m venv venv  

2. Activate virtual environment  
Mac/Linux - source venv/bin/activate  
Windows PowerShell - venv\Scripts\activate  

3. Install Playwright browsers  
playwright install  

## Run Tests
Run all tests  
pytest  

Run tests in headed mode  
pytest --headed  

## Page Object Model
- Each page has its own class
- Locators and actions are stored in page classes
- Tests contain only test logic
- Improves maintainability and readability

## Notes
This project is created for learning and practice only.
