import time

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePageDemo(BaseClass):
    def test_HomePageDemo(self, setup, getData):
        log = self.getLoger()
        homePage = HomePage(self.driver)
        log.info("First name is "+getData["name"])
        homePage.getName().send_keys(getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(123456)
        homePage.getCheckbox().click()

        # Static Dropdown
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        # dropdown.select_by_index(1)
        # dropdown.select_by_visible_text("Male")

        homePage.getSubmitBtn().click()
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()

        message = homePage.getSuccessMsg().text
        print(message)
        assert "Success" in message
        print(self.driver.title)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.home_page_data)
    def getData(self, request):
        return request.param
