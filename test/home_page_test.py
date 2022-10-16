import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.home_page import Homepage
from src.pages.new_window_page import NewWindowPage
from src.pages.new_tab_page import NewTabPage
from selenium.webdriver.support import expected_conditions as EC


def test_load_page_successful(driver):
    wait = WebDriverWait(driver, timeout=10)
    homepage = Homepage(driver)
    new_tab_page = NewTabPage(driver)

    driver.get(homepage.url)
    assert driver.current_url == homepage.url


def test_suggestion_countries(driver):
    homepage = Homepage(driver)
    homepage.countries_input.send_keys("Me")
    homepage.select_country_by_text("Mexico")
    print("TEST")
    print(homepage.countries_input.get_attribute("value"))
    assert homepage.countries_input.get_attribute("value") == "Mexico"


def test_drop_down_options(driver):
    homepage = Homepage(driver)
    homepage.select_by_option_number("2")
    assert homepage.get_selected_option() == "option2"
    homepage.select_by_option_number("3")
    assert homepage.get_selected_option() == "option3"


def test_window_example_load_successful(driver):
    homepage = Homepage(driver)
    new_window_page = NewWindowPage(driver)
    homepage.open_windows_button.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.url_contains(new_window_page.url))
    assert driver.current_url == new_window_page.url


def test_window_example_title_self_paced(driver):
    new_window_page = NewWindowPage(driver)
    title = new_window_page.get_welcome_title("1")
    assert title == "SELF PACED ONLINE TRAINING"


def test_window_example_title_in_depth(driver):
    new_window_page = NewWindowPage(driver)
    title = new_window_page.get_welcome_title("2")
    assert title == "IN DEPTH MATERIAL"


def test_window_example_title_lifetime(driver):
    new_window_page = NewWindowPage(driver)
    title = new_window_page.get_welcome_title("3")
    assert title == "LIFETIME INSTRUCTOR SUPPORT"


def test_window_example_title_resume_preparation(driver):
    new_window_page = NewWindowPage(driver)
    title = new_window_page.get_welcome_title("4")
    assert title == "RESUME PREPARTION & INTERVIEW QUESTIONS"


def test_window_example_title_30_day_money_back(driver):
    new_window_page = NewWindowPage(driver)
    title = new_window_page.get_welcome_title("5")
    assert title == "30 DAY MONEY BACK GUARANTEE"
