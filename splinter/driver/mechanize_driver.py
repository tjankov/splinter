from lxml.cssselect import CSSSelector
from splinter.driver import DriverAPI, ElementAPI

import mechanize

class Mechanize(DriverAPI):
    pass
    
    def __init__(self):
        self.driver = mechanize.Browser()

    @property
    def title(self):
        return self.driver.title()

    @property
    def html(self):
        return self.response

    @property
    def url(self):
        return self.driver.geturl()

    def visit(self, url):
        self.driver.open(url)
        self.response = self.driver.response().read()

    def find_link_by_href(self, href):
        return MechanizeElement(self.driver.find_link(url=href))

    def find_link_by_text(self, text):
        return MechanizeElement(self.driver.find_link(text=text))
             
    def quit(self):
        self.driver.close()

class MechanizeElement(ElementAPI):

    def __init__(self, element):
        if isinstance(element, mechanize._html.Link):
            element.href = element.url
        self._element = element

    def __getitem__(self, attr):
        return getattr(self._element, attr)
