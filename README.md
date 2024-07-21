## Automation Framework for the Web Platform 

The automation framework for the web platform using selenium and python in the Page Object Model (POM) pattern and the unit testing framework to ensure fast validation is presented.

*   What is this repository for?
*   How do I get set up?
*   Important Notes
*   Who do I talk to?

### What is this repository for? 👽

This repository aims to reduce the manual validation effort in the QA process. The framework created could improve the regression flow when versions are produced. It also allows scalability to test pipes using CI. 

### How do I get set up? 🔥

* Install python (version = 3.7), this would be your python interpreter on Pycharm.
* Install Pycharm (the latest version): \<[https://www.jetbrains.com/es-es/pycharm/download/#section=windows](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)\>
  * Configure your interpreter:
    * Press `CTRL + ALT + S` - Settings modal will be displayed
    * Expand the `Project: ct-lm-web-app-qa` option
    * Click on `Python Interpreter`
    * Select your python - version = 3.7
* Git clone 
* Open the project that was cloned on Pycharm
* Create a different branch \<`dev_automation`\> on the Terminal
* Config the interpreter (venv folder of pipenv or in the `requirements` file you can find all the plugins needed to install)
    *   You can use the following command on the Pycharm Terminal to install all the dependencies \<`pip install -r requirements.txt`\>
* Once there are no red flags about the dependencies, it is time to execute the \<`test-xxx.py`\> and verify if it is working properly.

#### Running a specific script \<`test-001.py`\> on the terminal:

*   Open the terminal and send the following command: \<`nosetests -v [name of the specific test]`\>
    *   `nosetests -v [test_001.py]`
*   Send the following command through the terminal:: \<`nosetests -v tests=[list of tests]`\>
    *   `nosetests -v tests=[list of tests]`

#### Running a specific script \<`test-001.py`\> using Pycharm:

*   Right-click on the specific test \<`test-001.py`\> that you want to execute.
*   Select the "Run Python test" option
    *   A new section called "Result Toolbar" is displayed where you can see the Test Results.
        *   \# of scenarios were executed.
        *   \# of scenarios that passed, skipped, or failed.
        *   time of execution
        *   information for each scenario

#### Running the whole suite on the terminal:

*   Open the terminal and send the following command: \<`nosetests - v`\>

#### Running the whole suite using Pycharm:

*   Right-click on the "Test" folder (includes all the executions)
*   Select the "Run Python test" option
*   Review the results on the "Result toolbar"

#### Running the whole suite on the terminal generating reports:

*   Open the terminal and send the following command: \<`nosetests -v --with-xunit --xunit-file="../test-reports/summary_report.xml" --xunit-testsuite-name="Smoke Testing Validation for the Web Platform"`\>

### Important Notes 📚

* To generate visual reports you can install: \<`html-testRunner`\> \<`allure-behave`\> or \<`pytest-html-reports`\>
  * Make sure to include the "report library" in the `pip-requirements`.
* Make sure to create your `.env` file to set your own variables \<`local configuration`\>
* Make sure to avoid printing vulnerable credentials.

### Who do I talk to?

Do not hesitate to contact _**Marcia Gutiérrez**_ on Slack if you have some errors or concerns about the project. 
Any suggestion helps to improve the automation project! 🐜

**Free Software, Hell Yeah!**