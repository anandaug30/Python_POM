import unittest
from utilities import constants
from common.common_function import OpenBrowser


class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = OpenBrowser.load_application('chrome', constants.base_url['bus'], 'Online Bus Ticket Booking')

    def test_homepage(self):
        self.driver.title()

    def tearDown(self) -> None:
        self.driver.close()
