from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.home_page import Homepage
from src.pages.new_window_page import NewWindowPage
from src.pages.new_tab_page import NewTabPage
from selenium.webdriver.support import expected_conditions as EC


def test_load_page_successful(driver):
    homepage = Homepage(driver)
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


def test_new_window_example_load_successful(driver):
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


def test_window_example_text_for_lifetime(driver):
    new_window_page = NewWindowPage(driver)
    text = new_window_page.get_welcome_text("1")
    assert text == "You can access the videos on 24* 7 for Lifetime. You can access the videos in iPad/Mobile too."


def test_window_example_text_for_in_depth(driver):
    new_window_page = NewWindowPage(driver)
    text = new_window_page.get_welcome_text("2")
    assert text == "Top class material designed on all courses for making you better in depth understanding of the concepts taught in the lectures."


def test_window_example_text_for_lifetime(driver):
    new_window_page = NewWindowPage(driver)
    text = new_window_page.get_welcome_text("3")
    assert text == "We are happy to help you on any query in the course you are enrolled in. Trainer will reach out to you personally once you signup with the course."


def test_window_example_text_for_resume_preparation(driver):
    new_window_page = NewWindowPage(driver)
    text = new_window_page.get_welcome_text("4")
    assert text == "We will help you in preparing the resume and provide good number of Interview questions once you have completed the entire course."


def test_window_example_text_for_30_day(driver):
    new_window_page = NewWindowPage(driver)
    text = new_window_page.get_welcome_text("5")
    assert text == "We would never want you to be unhappy! If you are unsatisfied with your purchase, contact us in the first 30 days and we will give you a full refund."
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def test_window_tab_example_load_successful(driver):
    homepage = Homepage(driver)
    new_tab_page = NewTabPage(driver)
    homepage.open_tab_button.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.url_contains(new_tab_page.url))
    assert driver.current_url == new_tab_page.url


def test_window_tab_example_view_all_courses_button(driver):
    new_tab_page = NewTabPage(driver)
    new_tab_page.wait_preload_off()
    driver.execute_script("window.scrollTo(0,1800)")
    driver.save_screenshot('Screenshots/pageWithViewAllCoursesButton.png')
    new_tab_page.view_all_courses_button.screenshot('Screenshots/ViewAllCoursesButton.png')
    assert new_tab_page.view_all_courses_button.is_displayed()
    driver.switch_to.window(driver.window_handles[0])


def test_alert_msg_text(driver):
    homepage = Homepage(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(homepage.alert_input))
    homepage.alert_input.send_keys("Stori Card")
    homepage.alert_button.click()
    alert = Alert(driver)
    assert alert.text == "Hello Stori Card, Are you sure you want to confirm?"
    alert.accept()


def test_print_courses_by_price(driver):
    homepage = Homepage(driver)
    count = homepage.get_coursers_by_price("25")
    print(count)
    assert len(count) == 4


def test_print_engineer_names(driver):
    homepage = Homepage(driver)
    names = homepage.get_names_engineers()
    print(names)
    assert len(names) == 8


def test_text_mentorship_paragraph(driver):
    homepage = Homepage(driver)
    new_tab_page = NewTabPage(driver)
    driver.switch_to.frame(homepage.courses_iframe)
    text_paragraph = new_tab_page.get_paragraph_text(2)
    assert text_paragraph == "His mentorship program is most after in the software testing community with long waiting period."
