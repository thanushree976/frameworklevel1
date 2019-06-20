import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/dell/PycharmProjects/frameworklevel1/drivers/chromedriver.exe")
    driver.get("http://localhost:1287/login?from=%2F")
    driver.implicitly_wait(30)
    request.cls.driver = driver

    #yield
    #driver.quit()