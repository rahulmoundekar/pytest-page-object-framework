import pytest
from selenium import webdriver
import time

from pages.LoginPage import LoginPage


class TestLoginTest:
    baseURL = "https://admin-demo.nopcommerce.com/"
    driver = webdriver.Chrome()

    @pytest.fixture()
    def setUpClass(self):
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_login(self, setUpClass):
        login_page = LoginPage(self.driver)
        login_page.setUserName('admin@yourstore.com')
        login_page.setPassword('admin')
        login_page.clickOnLogin()
        time.sleep(5)

        assert self.driver.title == "Dashboard / nopCommerce administration"

        login_page.clickOnLogout()
