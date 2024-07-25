# STC Automation BDD Framework

## Overview

The STC Automation Test Framework is designed to validate subscription packages on the STC TV subscription page. This is a simple framework using Python with Behave for BDD testing. It supports different browsers through configurations. Console level logging is implemented.

## Key Approaches
### 1. Dynamic Driver Fetching Using Factory Pattern
This framework implements a factory pattern to handle the dynamic creation and configuration of WebDriver instances. This allows for flexible and easily configurable cross-browser testing with config file.

### 2. Dynamic Element Handling
Used flexible locators and dynamic methods to fetch package titles, prices, and currencies.

### 3. Dynamic Data Fetching
The framework dynamically fetches and test data to compare with page data.

### 4. POM 
POM for interacting with UI elements.

## Setup

### Prerequisites

1. **Python**: Ensure Python 3.6 or higher is installed.
2. **Pip**: Ensure pip is installed.

### Install Required Python Packages

```sh
pip install -r requirements.txt
 ```

### Running Tests
To run the tests, use the following command:

```sh
behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html
```
### Sample Report
![image](https://github.com/user-attachments/assets/04abd39b-bf92-46d1-8499-3879ee4145ee)


