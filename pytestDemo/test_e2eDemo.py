from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2eDemo(self, setup):
        log = self.getLoger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckOutPage(self.driver)
        log.info("Getting all the card titles")
        devices = checkoutPage.getCardTitles()

        #devices = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for device in devices:
            deviceName = device.find_element(By.XPATH, "div/h4/a").text
            log.info(deviceName)
            if deviceName == "Blackberry":
                #deviceName = checkoutPage.DeviceName()
                #checkoutPage.DeviceName().click()
                device.find_element(By.XPATH, "div/button").click()

        checkoutPage.checkOutButton().click()
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        #self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        checkoutPage.confirmCheckoutbtn().click()

        confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name as Ind")
        confirmPage.countryNames().send_keys("Ind")

        #self.driver.find_element(By.ID, "country").send_keys("Ind")

        # time.sleep(15)
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.countrySelection().click()
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.checkBox().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        #self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        confirmPage.confirmButton().click()

        message = self.driver.find_element(By.CSS_SELECTOR, "a[class='close']").text
        print(message)
        log.info("Text received from application is "+message)
        #assert "Success! Thank you! Your order will be delivered in next few weeks :-)" == message
