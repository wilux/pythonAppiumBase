import pytest


from src.pages.home_page import Homepage
from src.pages.login_page import SignInPage


@pytest.mark.smoky
def test_browserstack(driver):

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    driver.get(homepage.base_url)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    driver.quit()
