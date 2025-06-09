# Playwright Test Framework

This project is an automation test framework built using Playwright and Python for testing web UI applications. It provides a structured approach to writing and organizing tests, utilizing the Page Object Model (POM) for better maintainability and scalability.

## Project Structure

```
playwright-test-framework
├── src
│   ├── tests
│   │   └── test_sample.py      # Contains test cases for the web UI
│   ├── pages
│   │   └── base_page.py        # Base class for page objects
│   └── utils
│       └── helpers.py          # Utility functions for the test framework
├── requirements.txt             # Project dependencies
├── pytest.ini                   # Configuration for pytest
└── README.md                    # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd playwright-test-framework
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers:**
   After installing the dependencies, you need to install the Playwright browsers:
   ```bash
   playwright install
   ```

## Running Tests

To run the tests, use the following command:
```bash
pytest src/tests
```

## Usage Examples

- Add your test cases in `src/tests/test_sample.py`.
- Create specific page classes by inheriting from `BasePage` in `src/pages/base_page.py`.
- Utilize utility functions from `src/utils/helpers.py` as needed.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features. 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.