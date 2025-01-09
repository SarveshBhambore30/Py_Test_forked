from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
        #self.driver.find_element(By.ID, "country").send_keys("Ind")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    countries = (By.ID, "country")
    countryC = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmbtn = (By.CSS_SELECTOR, "input[type='submit']")

    def countryNames(self):
        return self.driver.find_element(*ConfirmPage.countries)

    def countrySelection(self):
        return self.driver.find_element(*ConfirmPage.countryC)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def confirmButton(self):
        return self.driver.find_element(*ConfirmPage.confirmbtn)
