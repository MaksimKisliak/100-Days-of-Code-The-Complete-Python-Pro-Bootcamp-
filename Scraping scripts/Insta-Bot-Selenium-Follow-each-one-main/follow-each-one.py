from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

USER_ID = "username"
ACCOUNT_PASSWORD = "password"
ACC = "cristiano"  # account whose followers you want to follow


class InstaFollower:
    def __init__(self):
        # Set Chrome options
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)

        # Create the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

        # Visit the Instagram login page
        self.driver.get("https://www.instagram.com/")

    def login(self):
        # Find the username input field and enter the USER_ID
        user_field = self.driver.find_element(by="name", value="username")
        user_field.send_keys(USER_ID)

        # Find the password input field and enter the ACCOUNT_PASSWORD
        password_field = self.driver.find_element(by="name", value="password")
        password_field.send_keys(ACCOUNT_PASSWORD)

        # Press the Enter key to submit the form
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        # Wait for the page to load
        time.sleep(5)

        # Navigate to the target account's profile page
        self.driver.get(f"https://www.instagram.com/{ACC}/")

        # Wait for the page to load
        time.sleep(2)

        # Find the followers button and click it
        followers = self.driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        # Wait for the page to load
        time.sleep(2)

    def follow(self):
        # Follow a specified number of followers
        for i in range(2):  # adjust as desired
            # Find the follow button
            button = self.driver.find_element(by="css selector", value="._acas:not(._acao), a._acas:not(._acao), a._acas:not(._acao):visited")

            try:
                # Click the follow button
                button.click()

                # Wait for the action to complete
                time.sleep(1)
            except ElementClickInterceptedException:
                # If the button is obscured, click the cancel button to close the dialog
                cancel_button = self.driver.find_element(by="xpath",value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
time.sleep(3)
bot.login()
bot.find_followers()
bot.follow()
