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
        return self._find_control_by_name(name)

    def find_link_by_href(self, href):
        return MechanizeLinkELement(self.driver.find_link(url=href))

    def find_link_by_text(self, text):
        return MechanizeLinkELement(self.driver.find_link(text=text))

    def fill_in(self, field_name, field_value):
        control = self._find_control_by_name(field_name)
        control.value = field_value

    def quit(self):
        self.driver.close()

    def _find_control_by_name(self, name):
        for form in self.driver.forms():
            for control in form.controls:
                if control.name == name:
                    return MechanizeControlElement(control)


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

class MechanizeControlElement(ElementAPI):

    def __init__(self, control):
        self._element = control

    def _get_value(self):
        return self._element._value

    def _set_value(self, value):
        self._element._value = value

    value = property(_get_value, _set_value)