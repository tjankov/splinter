from splinter.driver.webdriver import WebDriver
from splinter.driver.mechanize_driver import Mechanize

class Browser(object):

    _DRIVERS = dict(mechanize=Mechanize,
                    webdriver=WebDriver)

    def __init__(self, driver='webdriver'):
        driver_class = self._DRIVERS[driver]
        self._driver = driver_class()

    def __getattr__(self, attr):
        return getattr(self._driver, attr)
