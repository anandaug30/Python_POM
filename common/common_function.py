from utilities import constants
from selenium import webdriver


class OpenBrowser:
    @classmethod
    def load_application(cls, browser, url, title=""):
        driver = None
        if browser in constants.driver:
            if browser == 'chrome':
                driver = webdriver.Chrome(executable_path=constants.driver[browser])
                print('Browser {} is started '.format(browser))
            elif browser == 'ff':
                driver = webdriver.Firefox(executable_path=constants.driver[browser])
                print('Browser {} is started '.format(browser))
            elif browser == 'ie':
                driver = webdriver.Ie(executable_path=constants.driver[browser])
                print('Browser {} is started '.format(browser))
        else:
            print("No Such {} Driver defined yet")
        if driver is not None:
            driver.get(url)
            print('loading {}'.format(url))
            driver.maximize_window()
            if title != "":
                print(driver.title)
                assert title in driver.title

        return driver
