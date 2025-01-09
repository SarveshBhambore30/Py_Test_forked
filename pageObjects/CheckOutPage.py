from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    deviceName = (By.XPATH, "div/button")
    checkOutbtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    confirmCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def DeviceName(self):
        return self.driver.find_elements(*CheckOutPage.deviceName)

    #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutbtn)

    def confirmCheckoutbtn(self):
        return self.driver.find_element(*CheckOutPage.confirmCheckout)
