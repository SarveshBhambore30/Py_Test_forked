import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("headless")

    service_obj = Service("C:\\WebDrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(4)
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()

