from pages.loginpage import Login
from data.testdata import *
import  pytest


@pytest.mark.usefixtures("test_setup")



class TestLogin:
    def test_jenkinslogin(self):
        driver=self.driver
        lp=Login(driver)
        lp.jenkinslogin(USERNAME,PASSWORD)

#logout from app
#driver.find_element_by_xpath("//b[text()='log out']").click()