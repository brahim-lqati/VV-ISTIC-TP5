## Find a bug

Clone the [Simba Organizer repository](https://github.com/selabs-ur1/doodle) and follow the instructions to run the application on your machine.

Find a bug in the application. 

With the help of Selenium and the Page Object Model desing pattern write a simple test that fails for this bug.

Optionally make a pull request to the project.

Include in this document the code of the test and, if you did it, the link to the pull request.

## Answer

### Requirements
- [Python](https://www.python.org/downloads/)

You can install selenium and selenium-wire , using this command:
```bash
pip install selenium
pip install selenium-wire
```

**<<Comments Part in the page (exo 2)>>**
We have written a simple test that verifies the creation of a new comment using the Page Object Model (POM) created earlier.

To run the test, you need to modify the URL declared in the test [file](../Tests/find_bug_test.py) and set it to the link of the page requested in exercise 2.

In my case, I tested with a local address linked to a DNS.


##### First test:

The first test is aimed at verifying whether attempting to add a comment with an empty author name will result in errors. 

#### Second test:

For the second test, I utilized the selenium-wire package, which enabled us to capture the requests that were sent. In the application, after adding a comment, a request is sent to retrieve the comments. However, an error 404 was encountered. Therefore, I conducted a test that captures this bug.


#### Test run
To execute the test, you need to navigate to the root of the project and run the command:

```bash
python3 Tests/find_bug_test.py
```



