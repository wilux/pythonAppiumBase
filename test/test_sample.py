from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
import textwrap
import copy

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from helpers import report_to_sauce, take_screenshot_and_logcat, ANDROID_BASE_CAPS, EXECUTOR


class TestAndroidBasicInteractions():
    # PACKAGE = 'io.appium.android.apis'
    # SEARCH_ACTIVITY = '.app.SearchInvoke'
    # ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'

    @pytest.fixture(scope='function')
    def driver(self, request, device_logger):
        calling_request = request._pyfuncitem.name

        caps = copy.copy(ANDROID_BASE_CAPS)
        # caps['name'] = calling_request
        # caps['appActivity'] = self.SEARCH_ACTIVITY

        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=caps
        )

        def fin():
            report_to_sauce(driver.session_id)
            take_screenshot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)
        driver.implicitly_wait(10)
        driver.update_settings({"waitForIdleTimeout": 100})
        return driver

    def test_login(self, driver):
        userInput = driver.find_element(By.XPATH, "//*[@resource-id='username_test']")
        passwordInput = driver.find_element(By.XPATH, "//*[@resource-id='password_test']")
        submitButton = driver.find_element(By.XPATH, "//*[@resource-id='testID']")
        userInput.send_keys("rioshugo")
        passwordInput.send_keys("QAbpn2022")
        submitButton.click()
        accept_check = driver.find_element(By.XPATH, "//*[@resource-id='terms_checkbox_test']")
        accept_button = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]")
        accept_check.click()
        accept_button.click()
        txtWelcome = driver.find_element(By.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]")
        assert txtWelcome.text == 'Hola HUGO'
