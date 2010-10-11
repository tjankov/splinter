from splinter.driver.webdriver import WebDriver
from splinter.driver.mechanize_driver import Mechanize

class Browser(object):

    def __init__(self, driver='webdriver'):
        if driver == 'mechanize':
            self._driver = Mechanize()
        if driver == 'webdriver':    
            self._driver = WebDriver()

    def __getattr__(self, attr):
        return getattr(self._driver, attr)
