import unittest
from selenium import webdriver
import sys
import os

class AdminPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sys.path.append(os.getcwd())
        print(sys.path)
        cls.driver = webdriver.Chrome()
        cls.url = "http://doodle-kube.com/answer/6ctZ5MHCaSO2gR7Y50Nv7FWR"
    

    def test_add_comment_with_empty_data(self):
        from Pages.admin_page import AdminPage

        adminePage = AdminPage(self.driver, self.url)
        
        # add comment
        adminePage.enter_comment_author("   ")
        adminePage.enter_comment_content("sas  sa")

        adminePage.add_comment()

        # check if we get error
        # as you see, i put a string in author field that contains just spaces
        # we should get errors
        self.assertTrue((adminePage.get_errors() is not None) and len(adminePage.get_errors() > 0))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
