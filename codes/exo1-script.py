from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import random

driver = webdriver.Chrome()

# navigate to Wekipedia
driver.get('https://en.wikipedia.org/')


visited_link = []

links = None

i = 0

while i < 10:
    try:
        if links is None:
            # find href element (link)
            links = driver.find_elements(By.XPATH, "//a[@href]")
        
        # choose a random link
        link = random.choice(links)
        # avoid visiting links
        href = link.get_attribute("href")
        if href is not None and href not in visited_link and 'wikipedia' in href.lower():
            # until 2 sec until the link element will be_clickable
            wait = WebDriverWait(driver, 2)
            link = wait.until(EC.element_to_be_clickable(link))
            link.click()
            # sucess click
            # add link to visisted links list
            visited_link.append(href)
            # take screenshot
            driver.save_screenshot(f'screenshots/screenshot-{i+1}.png')
            i += 1
            # clear links for to get links from the new opening page
            links = None
    except TimeoutException:
        continue
    except NoSuchWindowException:
        continue

# Close the Chrome webdriver
driver.quit()