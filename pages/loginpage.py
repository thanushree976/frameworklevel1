from selenium import  webdriver
class Login:
    def __init__(self,driver):
        self.driver=driver
    def jenkinslogin(self,un,pwd):
        # Login
        self.driver.find_element_by_id("j_username").send_keys(un)
        self.driver.find_element_by_name("j_password").send_keys(pwd)
        self.driver.find_element_by_name("Submit").click()

