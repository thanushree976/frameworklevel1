from pages.webgeneric import WebGeneric
class Login(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.driver = driver
        self.un_id="j_username"
        self.pwd_name="j_password"
        self.log_in="Submit"

    def jenkinslogin(self,un,pwd):
        wg=WebGeneric(self.driver)
        wg.enter(self.un_id,un)
        wg.enter(self.pwd_name,pwd)
        wg.submit(self.log_in)






        # Login
        #self.driver.find_element_by_id("j_username").send_keys(u n)
        #self.driver.find_element_by_name("j_password").send_keys(pwd)
        #self.driver.find_element_by_name("Submit").click()

