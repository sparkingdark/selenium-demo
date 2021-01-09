import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
      
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")

        self.assertIn("Python",driver.title)

        elem = driver.find_element_by_name("q")

        elem.send_keys("pycons")
        elem.send_keys(Keys.RETURN)

        assert "No Result found" not in driver.page_source

    def teardown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
