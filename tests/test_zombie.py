import unittest
from splinter.browser import Browser
from base import BaseBrowserTests
from fake_webapp import EXAMPLE_APP


class ZombieTest(BaseBrowserTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('zombie')

    def setUp(self):
        self.browser.visit(EXAMPLE_APP)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
