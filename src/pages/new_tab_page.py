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
        "preloaded_off": ("XPATH", "//div[@class='preloader'][contains(@style,'display: none')]")
    }

    def get_paragraph_text(self, order):
        element = ".price-title div:nth-of-type(2) li:nth-of-type(" + order + ")"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.driver.find_element(By.find_element_by_css, element).text

    def wait_preload_off(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='preloader'][contains(@style,'display: none')]")))
