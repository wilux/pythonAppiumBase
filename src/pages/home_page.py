from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rahulshettyacademy.com/AutomationPractice/"

    locators = {
        "countries_input": ("XPATH", "//input[@id='autocomplete']"),
        "dropdown_select": ("XPATH", "//select[@id='dropdown-class-example']"),
        "open_windows_button": ("XPATH", "//button[@id='openwindow']"),
        "open_tab_button": ("XPATH", "//a[@id='opentab']"),
        "alert_input": ("XPATH", "//input[@id='name']"),
        "alert_button": ("XPATH", "//input[@id='alertbtn']"),
        "courses_table": ("//table[@name='courses']/tbody[1]/tr"),
        "fixed_table": ("//fieldset[contains(.,'Web Table Fixed header')]//table[@id='product']/tbody[1]/tr"),
        "courses_iframe": ("CSS", "#courses-iframe")
    }

    def select_country_by_text(self, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//ul[@class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front']//div[.='" + text + "']"))).click()

    def select_by_option_number(self, number):
        drpCountry = Select(self.dropdown_select)
        drpCountry.select_by_value("option" + number)

    def get_selected_option(self):
        return self.dropdown_select.get_attribute("value")

    def get_coursers_by_price(self, price):
        labels_list = []
        for n in self.fet_coursers_by_price.size:
            try:
                name = self.driver.find_element(By.XPATH, "//table[@id='product']/tbody[1]/tr[" + n + "]/td[3]")
                if name.text == price:
                    print_name = self.driver.find_element(By.XPATH,
                                                          "//table[@name='courses']/tbody[1]/tr[" + n + "]/td[2]").text
                    labels_list.append(print_name)
                    print(print_name)
            finally:
                print("An exception occurred")
            return labels_list

    def get_names_engineers(self):
        labels_list = []
        for n in self.fet_coursers_by_price.size:
            name = self.driver.find_element(By.XPATH,
                                            "//fieldset[contains(.,'Web Table Fixed header')]//table[@id='product']/tbody[1]/tr[" + n + "]/td[1]")
            labels_list.append(name)
            print(name)
            return labels_list
