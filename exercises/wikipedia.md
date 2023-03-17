# Random Wikipedia walker

Using Selenium, create a small program that, starting from the main page https://www.wikipedia.org/, walks trough a sequence of random links and takes a snapshot of the last page.
The process is as follows:

 1. Navigate to the main page https://www.wikipedia.org/
 2. Select a random link in the page
 3. Navigate to the link
 4. Repeat steps 2 to 3 until you have visited 10 different pages
 5. Take a snapshot of the current page and save it

Include the code of the walker and the snapshot in this document.

## Answer

### Requirements
- [Python](https://www.python.org/downloads/)

You can install selenium, using this command:
```bash
pip install selenium
```
I wrote the script in python, you can find it [here](../codes/exo1-script.py)

To execute the script, You can run this command
```bash
python3 exo1-script.py
```

