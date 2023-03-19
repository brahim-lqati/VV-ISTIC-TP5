## Find a bug

Clone the [Simba Organizer repository](https://github.com/selabs-ur1/doodle) and follow the instructions to run the application on your machine.

Find a bug in the application. 

With the help of Selenium and the Page Object Model desing pattern write a simple test that fails for this bug.

Optionally make a pull request to the project.

Include in this document the code of the test and, if you did it, the link to the pull request.

## Answer

**<<Comments Part in the page (exo 2)>>**
We have written a simple test that verifies that an error should be raised if we try to add an author name that contains an empty string. We have used the Page Object Model (POM) created earlier.

To run the test, you need to modify the URL declared in the test [file](../Tests/find_bug_test.py) and set it to the link of the page requested in exercise 2.

In my case, I tested with a local address linked to a DNS.

To execute the test, you need to navigate to the root of the project and run the command:

```bash
python3 Tests/find_bug_test.py
```


