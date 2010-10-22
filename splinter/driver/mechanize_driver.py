from lxml.cssselect import CSSSelector
from splinter.driver import DriverAPI, ElementAPI

import mechanize
import lxml.html as lhtml

class Mechanize(DriverAPI):
    
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

    def find_by_id(self, id):
        _html = lhtml.fromstring(self.response)
        return MechanizeElement(_html.get_element_by_id(id=id))

    def find_by_css_selector(self, css_selector):
        selector = CSSSelector(css_selector)
        _html = lhtml.fromstring(self.response)
        return MechanizeElement(_html.cssselect(css_selector)[0])
        
    def find_by_xpath(self, xpath):
        _html = lhtml.fromstring(self.response)
        return MechanizeElement(_html.xpath(xpath)[0])
        
    def find_by_tag(self, tag):
        return self.find_by_xpath('//%s' % tag)
        
    def find_by_name(self, name):
        return self.find_by_xpath("//*[@name='%s']" % name)

    def find_link_by_href(self, href):
        return MechanizeLinkELement(self.driver.find_link(url=href))

    def find_link_by_text(self, text):
        return MechanizeLinkELement(self.driver.find_link(text=text))
             
    def quit(self):
        self.driver.close()
        
class MechanizeLinkELement(ElementAPI):

    def __init__(self, element):

        element.href = element.url
        self._element = element

    def __getitem__(self, attr):
        return getattr(self._element, attr)
    
class MechanizeElement(ElementAPI):

    def __init__(self, element):
        self._element = element
    
    @property
    def value(self):
        if self._element.text_content() == '':
            return self._element.value
            
        return self._element.text_content()

    def __getitem__(self, attr):
        return getattr(self._element, attr)
