import pytest
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Setup commandline parameter for select browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="select browser",
        choices=("firefox", "edge", "chrome")
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Setup webdriver for different browsers
@pytest.fixture(scope="session")
def driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Added marks for tests
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoky:"
    )
    config.addinivalue_line(
        "markers", "functional:"
    )
