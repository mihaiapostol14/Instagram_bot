import os
import pickle

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from config import (
    USER_AGENT,
    ACCOUNT_USERNAME,
    ACCOUNT_PASSWORD
)
from helper import (
    Helper,
    DriverHelper,
    ElementChecker,
    create_temp_file
)


class InstagramBot(Helper):
    def __init__(self, account_username='', account_password='', requested_account_url=''):
        # Initialize Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("general.useragent.override",
                                    USER_AGENT)  # Set custom user agent to avoid detection as a bot
        self.options.set_preference("dom.webdriver.enabled", False)  # Disable WebDriver detection
        self.options.set_preference("intl.accept_languages", 'en-us')  # Set language WebDriver
        self.options.set_preference("dom.webnotifications.enabled", False)  # Disable WebDriver notifications

        self.service = Service(executable_path='GeckoDriver/geckodriver.exe')  # Path to WebDriver

        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)  # Create a new instance of the Firefox WebDriver with the specified options

        self.account_username = account_username
        self.account_password = account_password
        self.requested_account_url = requested_account_url

        self.driver_helper = DriverHelper(driver=self.driver)
        self.checker = ElementChecker(driver=self.driver)

        self.upload_cookies()


    def login_user(self):
        """
        This method is for login user and getting cookies
        """
        self.driver_helper.send_by_url(url='https://www.instagram.com/')
        self.driver.implicitly_wait(5)
        if self.checker.class_exists(class_name='_aa4a'):

            # TODO: login user
            try:
                username_field = self.driver.find_element(By.NAME, 'username')
                username_field.clear()
                username_field.send_keys(self.account_username)
                self.driver.implicitly_wait(3)

                password_field = self.driver.find_element(By.NAME, 'password')
                password_field.clear()
                password_field.send_keys(self.account_password, Keys.ENTER)
                self.random_pause_code(start=1, stop=20)

                self.driver.find_element(
                    By.CLASS_NAME, 'x1i10hfl' # Rejection saving data to login user
                ).click()

                # TODO: getting cookies
                self.create_directory(name_directory='cookies')
                pickle.dump(
                    self.driver.get_cookies(),
                    open(f'cookies/{self.account_username}_cookies', mode='wb')
                )
                self.random_pause_code(start=1, stop=11)


            except Exception as ex:
                print(ex)
                print('nn')
            self.driver_helper.close_driver()

    def get_account_post(self, account_name=''):

        self.driver_helper.send_by_url(url=f'https://www.instagram.com/{account_name}/')
        self.random_pause_code(start=1, stop=5)
        create_temp_file(data=account_name)

        self.create_directory(name_directory=account_name)

        photo_posts = None
        reel_posts = None
        all_posts = None

        try:
            for i in range(1,5):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.random_pause_code(start=1, stop=7)

                photo_posts = [photo.get_attribute('href') for photo in self.driver.find_elements(By.TAG_NAME, 'a') if '/p/' in photo.get_attribute('href')]

                reel_posts = [reel.get_attribute('href') for reel in self.driver.find_elements(By.TAG_NAME, 'a') if '/reel/' in reel.get_attribute('href')]

                all_posts = photo_posts + reel_posts

            # TODO: written photo posts in a text file
            self.create_file_from_list(
                filename=f'{account_name}/photo_posts.txt',
                data_list=photo_posts
            )

            # TODO: written all posts in text file
            self.create_file_from_list(
                filename=f'{account_name}/reel_posts.txt',
                data_list=reel_posts
            )

            # TODO: written all posts in text file
            self.create_file_from_list(
                filename=f'{account_name}/all_posts.txt',
                data_list=all_posts
            )


        except NoSuchElementException:
            ...
        self.driver_helper.close_driver()

    def upload_cookies(self):
        """upload cookies"""
        try:
            if os.path.exists('cookies'):
                self.driver_helper.send_by_url(url='https://www.instagram.com/')
                for cookies in pickle.load(
                        open(f'cookies/{self.account_username}_cookies', mode='rb')
                ):
                    self.driver.add_cookie(cookie_dict=cookies)
                self.random_pause_code(start=1, stop=5)
                self.driver.refresh() # refresh page
                self.random_pause_code(start=1, stop=5)
                self.get_account_post(account_name=self.requested_account_url.split('/')[3])

            else:
                return self.login_user()
        except FileExistsError as ex:
            print(ex)
            self.driver_helper.close_driver()




def main():
    requested_account_url = input('Please Enter Account Url: ').strip()

    return InstagramBot(
        account_username=ACCOUNT_USERNAME,
        account_password=ACCOUNT_PASSWORD,
        requested_account_url=requested_account_url
    )


if __name__ == '__main__':
    main()
