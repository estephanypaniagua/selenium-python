# <img src="https://www.svgrepo.com/show/473780/selenium.svg" width="100" height="100"> UI Automation using Selenium + Python

## Introduction

This is a project that call the page demo evershop to make a buy and test it. It also has a pipeline for running the tests using [Github Actions](https://github.com/estephanypaniagua/selenium-python/actions) and [Github Pages](https://estephanypaniagua.github.io/selenium-python/#dashboard) 

You can see the test result here: https://estephanypaniagua.github.io/selenium-python/#dashboard

## Coverage
This project covers the following scenarios and practices:

### Automation
1. Buy 3 differents products

## Tech Stack
- Selenium
- Python + Pytest
- Github Actions + Github Pages

## Project Structure
```
└── .github
│      └── workflows
│           └── test.yml
└── report
└── scrapper
│      └── utils
│      │    └── __init.py__.py
│      │    └── driver.py
|      |    └── generator.py
|      |    └── tools.py
│      └── views
│      |    └── __init__.py
│      └── __init__.py
│      └── scrapper.py
│      └── test_buy_products.py
└── .gitignore
└── README.md
└── requirements.txt
```

## Pre-requisites

1. [Python >= 3](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html).
2. Libraries obtained since requirements

## Project Setup since Linux machine

1. Clone this repository.
2. Navigate to the project folder using the terminal.
3. Run the commands:
``` bash
# install requirements
pip install -r requirements.txt

# run test and generate report
pytest --html-report=./report/index.html
```
