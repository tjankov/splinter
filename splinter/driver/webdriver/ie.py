# -*- coding: utf-8 -*-

from selenium.webdriver.ie.webdriver import WebDriver as IE

from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from splinter.driver.webdriver.cookie_manager import CookieManager


class WebDriver(BaseWebDriver):
    def __init__(self, *args, **kwargs):
        self.driver = IE()

        self.element_class = WebDriverElement
        self._cookie_manager = CookieManager(self.driver)
        super(WebDriver, self).__init__(*args, **kwargs)
