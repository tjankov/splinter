# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from base import WebDriverTests
from fake_webapp import EXAMPLE_APP
from splinter.browser import Browser
from tests import Namespace

ns = Namespace()


def setUpModule():
    ns.browser = Browser('ie')


def tearDownModule():
    ns.browser.quit()


class IEBrowserTest(WebDriverTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = ns.browser

    def setUp(self):
        self.browser.visit(EXAMPLE_APP)
