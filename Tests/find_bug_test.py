import unittest
from seleniumwire import webdriver
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
        """Add comment using empty data"""
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
    
    def test_add_valid_comment(self):
        """ Test add comment action
        The application send a request after a sucessful request to get comment
        we will capture this request
        """
        from Pages.admin_page import AdminPage

        adminePage = AdminPage(self.driver, self.url)
        
        # add comment
        adminePage.enter_comment_author("author")
        adminePage.enter_comment_content("content")

        adminePage.add_comment()

        add_comment_req = self.driver.wait_for_request('/api/poll/comment/*')

        # verify status code
        self.assertTrue(int(add_comment_req.response.status_code / 100) == 2)

        # by default the application send after and add command, another request to get comments
        # we capture the matching requests, and we check the status

        for req in self.driver.requests:
            # filter comment request
            if '/comment'in req.path:
                self.assertEquals(int(req.response.status_code / 100), 2)




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
