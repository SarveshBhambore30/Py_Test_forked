from selenium.webdriver.common.by import By


class HomePage:
    # Constructor created for the HomePage class for driver variables
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.ID, "exampleFormControlSelect1")
    alertText = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.alertText)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
