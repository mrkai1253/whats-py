import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Whatspy:
    def __init__(self, sleep_time):
        '''
        :param sleep_time: latency used for the purpose to scan qr code

        '''

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com")
        time.sleep(sleep_time)


    def send_message(self, receiver, message):
        search_box = self.driver.find_element_by_class_name('copyable-text')
        search_box.send_keys(receiver + Keys.ENTER)
        message_box = self.driver.find_element_by_class_name('_2S1VP')
        message_box.send_keys(message + Keys.ENTER)
        self.driver.save_screenshot('{0}.png'.format(time.time()))

    def quit_browser(self):
        self.driver.quit()


# test
whatspy = Whatspy(6)

user = raw_input("User name?")
n = int(raw_input("Count"))



for _ in range(n):
	whatspy.send_message(user, 'Automated message')
whatspy.quit_browser()
