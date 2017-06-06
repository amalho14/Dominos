## Continuous Integration Pipeline-Python-Pytest-Selenium-SauceLabs
[![Build Status](https://travis-ci.org/amalho14/Dominos.svg?branch=master)](https://travis-ci.org/amalho14/Dominos)

This code is meant for building Continuous Integration pipeline using Python.
It demonstrates the use of Selenium in conjunction with Sauce Labs for parallel test execution.

### Environment Setup

1. Global Dependencies
    * The recommended version of Python 2.7 [Install Python](https://www.python.org/downloads/) 
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation

2. Sauce Labs Credentials
    * In the terminal export your Sauce Labs Credentials as environmental variables:
    ```
    $ export SAUCE_USERNAME=<your Sauce Labs username>
	$ export SAUCE_ACCESS_KEY=<your Sauce Labs access key>
    ```
3. Project
	* The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
	```$ pip install virtualenv```
	* Create a virtual environment in your project folder the environment name is arbitrary.
	```$ virtualenv venv```
	* Activate the environment:
	```$ source venv/bin/activate```
	* Install the required packages:
	```$ pip install -r requirements.txt```
    
### Running Tests:  -n option designates number of parallel tests and -s to disable output capture.

*  Tests in Parallel:
    ```$ py.test -s -n 8 tests```

### Troubleshooting/Recommendation:

* To view live testing go to Sauce Labs Dashboard: [Sauce Labs](https://saucelabs.com/)

* Might face latency when connecting to Sauce Labs using Selenium Remote WebDriver. Selenium Waits may need to be increased. 


### Resources
##### [Sauce Labs Documentation](https://wiki.saucelabs.com/)

##### [Pytest Documentation](http://pytest.org/latest/contents.html)

##### [Selenium Documentation](http://www.seleniumhq.org/docs/)
