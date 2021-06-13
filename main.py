from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

PROMISSED_UP = 10
PROMISSED_DOWN = 100
LOGIN = "INST MAIL LOGIN test"
PASSWORD = "INSTA PASS q"
CHROME_DRIVER_PATH = "D:\Python_projects\python_tools\chromedriver.exe"

class InstaFollower:
    def __init__(self):
        self.deriver = webdriver.Chrome(CHROME_DRIVER_PATH)
        pass

    def login(self):
        self.deriver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        login_field=self.deriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_field=self.deriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_field.send_keys(LOGIN)
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(4)
        # Cancel two pop up windows
        self.deriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)
        self.deriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)

    def find_followers(self):
        self.deriver.get("https://www.instagram.com/bikepackingcom/?hl=ru")
        time.sleep(8)
        self.deriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').click()
        time.sleep(3)
        popup_followers = self.deriver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.follow()
            self.deriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup_followers)
            time.sleep(3)

    def follow(self):
        buttons = self.deriver.find_elements_by_css_selector("li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.deriver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()



insta=InstaFollower()
insta.login()
insta.find_followers()