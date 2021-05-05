from selenium import webdriver
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class internet:

    def __init__(self, path):
        self.path = path

    def openBrowser(self, link, username, password):
        self.browser = webdriver.Chrome(self.path)

        self.browser.get(link)

        time.sleep(2)

        # Cookies
        cookiesButton = self.browser.find_elements_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/button[1]')
        print(len(cookiesButton))

        cookiesButton[0].click()

        time.sleep(2)

        # Connect
        connectButton = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
        connectButton.click()

        time.sleep(2)

        # Fill in credentials
        userField = self.browser.find_elements_by_name('username')
        pasField = self.browser.find_element_by_name('password')

        userField[0].send_keys(username)
        pasField.send_keys(password)
        submitButton = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div')
        submitButton.click()

        time.sleep(5)

        # Don't save anything
        saveCredentialsButton = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        saveCredentialsButton.click()

        print('clicked')

        time.sleep(2)

    def commenting(self, comments):
        comment = random.choice(comments)

        commentButton = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button')
        commentButton.click()

        commentField = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        commentField.send_keys(comment)

        time.sleep(5)

        '''
        commentPostButton = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
        commentPostButton.click()
        '''
