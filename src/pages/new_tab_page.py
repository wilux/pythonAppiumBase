from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewTabPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.rahulshettyacademy.com/"
        self.wait = WebDriverWait(self, timeout=10)

    locators = {
        "view_all_courses_button": ("XPATH", "//a[.='VIEW ALL COURSES']"),
        "preloaded_off": ("XPATH", "//div[@class='preloader'][contains(@style,'display: none')]"),
    }

    def get_paragraph_text(self, order):
        return self.driver.find_element_by_css(".price-title div:nth-of-type(2) li:nth-of-type(" + order + ")").text

    def wait_preload_off(self):
        self.wait.until(EC.presence_of_element_located(self.preloaded_off))
