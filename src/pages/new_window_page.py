from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewWindowPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://www.qaclickacademy.com/"
        self.wait = WebDriverWait(self, timeout=10)

    locators = {
        "countries_input": ("XPATH", "//input[@id='autocomplete']"),
        "dropdown_select": ("XPATH", "//select[@id='dropdown-class-example']"),
        "open_windows_button": ("XPATH", "//button[@id='openwindow']")
    }

    def get_welcome_title(self, order):
        element = "(//div[@class='col-sm-9']//h3)[" + order + "]"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.driver.find_element(By.XPATH, element).text

    def get_welcome_text(self, order):
        element = "(//div[@class='col-sm-9']//p)[" + order + "]"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.driver.find_element(By.XPATH, element).text
