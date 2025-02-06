This project provides an automation framework for UI and API testing using Selenium, Pytest. 
It also integrates with GitHub Actions for CI/CD execution.

The Project Structure is setup as below:
/ui_test_framework
- tests/
---| test_ui.py        # UI tests using Selenium
- pages/
---| home_page.py      # Page Object Model for UI tests
- config/
---| config.yaml       # Configuration settings
- utils/
---| logger.py         # logging to file
- reports/              # Reports for test execution
- requirements.txt      # Dependencies to run Project
- README.md             # Documentation about the project #This document#
- pytest.ini            # Pytest config
- .github/workflows/
---| ci.yml            # GitHub Actions CI/CD pipeline

Steps to run/setup tests

- Clone the repository running from terminal:
git clone https://github.com/nnakrani/ui_test_framework.git
cd ui_test_framework

- Install the dependencies:
pip install -r requirements.txt

- Run the Python(Pytest)/Selenium tests using: (Logs and screenshots will be saved in the reports/ folder.)
pytest tests/test_ui.py --html=reports/ui_report.html

- Logging will be stored in logs/test_execution.log
