from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    """Template for all pages in the application.
    define the commom functionalities
    """
    def __init__(self, driver):
        # driver
        self.driver = driver
        ''' max waiting time'''
        self.wait = 5
    

    def click(self, locator):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(locator)).click()
    

    def enter_text(self, locator, value):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(locator)).send_keys(value)
    

    def get_text(self, locator):
        elmt = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(locator))
        return elmt.get_attribute("value")


    def get_value(self, locator):
        elmt = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(locator))
        return elmt.text


    def is_selected(self, locator):
        elmt = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(locator))
        return elmt.is_selected()


    def get_elements(self, locator):
        return WebDriverWait(self.driver, self.wait).until(EC.presence_of_all_elements_located(locator))

    def get_element(self, locator):
        return WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(locator))
    


    


