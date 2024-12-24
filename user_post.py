import os
import pickle
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import (
    USER_AGENT,
    ACCOUNT_USERNAME,
    ACCOUNT_PASSWORD
)
from helper import (
    Helper,
    user_option_list,
    Downloader, read_temp_file
)
import instaloader

class UserPost(Helper, Downloader):
    def __init__(self, account_username='', account_password='', user_option='', dir_name=''):
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
        self.user_option = user_option
        self.dir_name = dir_name
#        self.mouse_event = ActionChains(self.driver)

        self.upload_cookies()

    def xpath_exists(self, xpath):
        """Checks if an element with the given XPath exists on the page."""
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def css_selector_exists(self, css_selector):
        """Checks if an element with the given css_selector exists on the page."""
        try:
            # Attempt to find the element by css_selector
            self.driver.find_element(By.CSS_SELECTOR, css_selector)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def id_exists(self, element_id):
        """Checks if an element with the given ID exists on the page."""
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.ID, element_id)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def class_exists(self, class_name):
        """Checks if an element with the given class name exists on the page."""
        try:
            # Attempt to find the element by class name
            self.driver.find_element(By.CLASS_NAME, class_name)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def tag_exists(self, tag_name):
        """Checks if an element with the given Tag exists on the page."""
        try:
            # Attempt to find the element by Tag
            self.driver.find_element(By.XPATH, tag_name)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def send_by_url(self, url):
        """
        Navigates to the specified URL using the web driver.
        """
        # Use the web driver to open the specified URL
        self.driver.get(url=url)

    def iteration_by_post(self,filename):
        # iteration by post link form list
        with open(file=filename, mode='r') as file:
            source = file.read().split()
            return source # output list

    def like_post(self):
        """
        Iterates through posts and ensures each post is liked.

        This method automates the process of interacting with Instagram posts by:
        1. Reading a list of post URLs from a file (e.g., 'all_posts.txt').
        2. Navigating to each post's URL.
        3. Checking whether the post is already liked.
        4. Clicking the like button if the post is not liked.

        Steps:
        - Random pauses are introduced between actions to mimic human behavior.
        - The presence of the like button is verified using class names and CSS selectors.
        - If the post is already liked, a message is printed to the console.
        - Errors during interaction are caught and logged.

        Dependencies:
        - iteration_by_post: Reads post URLs from a file and iterates through them.
        - random_pause_code: Introduces random delays to simulate human-like interaction.
        - send_by_url: Navigates to a given URL.
        - class_exists: Checks if a specified class exists on the page.
        - css_selector_exists: Verifies the presence of an element using a CSS selector.

        Limitations:
        - Relies on Instagram's current DOM structure, which may change.
        - Excessive actions may trigger Instagram's anti-bot mechanisms.
        - Only handles NoSuchElementException errors explicitly.

        Potential Enhancements:
        - Use more stable 'css selector' for element detection.
        - Implement detailed error logging and retry mechanisms.
        - Add session persistence to avoid repeated logins.
        """
        for url in self.iteration_by_post(filename=f'{self.dir_name}/all_posts.txt'):
            self.random_pause_code(start=1, stop=7)

            try:
                # Navigate to the post URL
                self.send_by_url(url=url)
                self.random_pause_code(start=1, stop=7)

                # Check if the like button exists
                if self.class_exists(class_name='_aagw'):
                    self.random_pause_code(start=1, stop=7)

                    # Locate the like button by its CSS selector attribute
                    if self.css_selector_exists(css_selector='.xxk16z8 > title:nth-child(1)'):
                        print('post is liked')

                    else:
                        self.driver.find_element(By.CSS_SELECTOR, '.xp7jhwk > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').click()



            except NoSuchElementException as ex:
                print(f"Error interacting with the post at {url}: {ex}")

        # Close the driver after processing all posts
        return self.close_driver()

    def get_photo_from_post(self):
        for url in self.iteration_by_post(filename=f'{self.dir_name}/photo_posts.txt'):
            self.random_pause_code(start=1, stop=7)

            try:
                self.send_by_url(url=url)
                self.random_pause_code(start=1, stop=7)
                if self.class_exists(class_name='_acng'):

                    image_count = self.driver.find_elements(By.CLASS_NAME, '_acnb')
                    for index in range(1, len(image_count) + 1):
                        self.random_pause_code(start=1, stop=7)
                        self.send_by_url(url=f'https://www.instagram.com/{self.driver.current_url.split("/")[3]}/p/{self.driver.current_url.split("/")[5]}/?img_index={index}')
                        self.random_pause_code(start=1, stop=7)

                        if self.class_exists(class_name='_aagv'):

                            photo_src = self.driver.find_element(By.CLASS_NAME, '_aagv').find_element(By.TAG_NAME, 'img').get_attribute('src')

                            self.crate_file(
                                filename=f'{self.dir_name}/photo_src.txt',
                                mode='a',
                                data=photo_src
                            )

                else:
                    photo_src = self.driver.find_element(By.CLASS_NAME, '_aagv').find_element(By.TAG_NAME,
                                                                                              'img').get_attribute(
                        'src')

                    self.crate_file(
                        filename=f'{self.dir_name}/photo_src.txt',
                        mode='a',
                        data=photo_src
                    )


            except NoSuchElementException:
                ...
            if self.driver.current_url == self.iteration_by_post(filename=f'{self.dir_name}/photo_posts.txt')[-1]:
                self.close_driver()

                self.remove_duplicate(
                    default=f'{self.dir_name}/photo_src.txt',
                    sorted_filename=f'{self.dir_name}/photo_src_unique.txt',
                )
                self.random_pause_code(start=1, stop=5)

                self.downloader(
                    filename=f'{self.dir_name}/photo_src_unique.txt',
                    dir_name=f'{self.dir_name}/{self.dir_name}_photo',
                )

    def get_reel(self):

        for url in self.iteration_by_post(filename=f'{self.dir_name}/reel_posts.txt'):
            self.random_pause_code(start=1, stop=7)

            try:
                self.send_by_url(url=url)  # Navigate to the Reel's URL
                self.random_pause_code(start=1, stop=7)
                if self.class_exists(class_name='x5yr21d'):
                    self.random_pause_code(start=1, stop=7)

                # Initialize Instaloader with custom options
                L = instaloader.Instaloader(
                    download_pictures=False,  # Do not download pictures
                    download_videos=True,  # Download videos
                    dirname_pattern=f"{self.dir_name}/{self.dir_name}_reels",  # Set custom directory for downloads
                    download_video_thumbnails=False,  # Do not download video thumbnails
                    download_comments=False,  # Do not download comments
                    download_geotags=False,  # Do not download geotags
                    save_metadata=False,  # Do not save metadata
                    post_metadata_txt_pattern='',  # Custom metadata pattern for posts
                    storyitem_metadata_txt_pattern='',  # Custom metadata pattern for stories
                    filename_pattern="{profile}_{shortcode}"  # Custom filename pattern
                )

                # URL of the Instagram Reel
                reel_url = url

                # Download the reel
                L.download_post(instaloader.Post.from_shortcode(L.context, reel_url.split("/")[-2]), target='')



            except NoSuchElementException:
                print(f"No video element found for URL: {url}")

            # Close the driver if at the last URL
            if self.driver.current_url == self.iteration_by_post(filename=f'{self.dir_name}/reel_posts.txt')[-1]:
                return self.close_driver()

            # Close the driver if at the last URL
            if self.driver.current_url == self.iteration_by_post(filename=f'{self.dir_name}/reel_posts.txt')[-1]:
                return self.close_driver()

    def select_option(self, option=''):
        match option:
            case '1':
                return self.like_post()
            case '2':
                return self.get_photo_from_post()
            case '3':
                return self.get_reel()
    

    def upload_cookies(self):
        try:
            if os.path.exists('cookies'):
                self.send_by_url(url='https://www.instagram.com/')
                for cookies in pickle.load(
                        open(f'cookies/{self.account_username}_cookies', mode='rb')
                ):
                    self.driver.add_cookie(cookie_dict=cookies)
                self.random_pause_code(start=1, stop=5)
                self.driver.refresh()
                self.random_pause_code(start=1, stop=5)
                return self.select_option(option=self.user_option)


            else:
                ...
        except FileExistsError as ex:
            print(ex)
        self.close_driver()

    def close_driver(self):
        """Close driver"""

        self.driver.close()
        self.driver.quit()


def main():
    return UserPost(
        account_username=ACCOUNT_USERNAME,
        account_password=ACCOUNT_PASSWORD,
        dir_name=read_temp_file(), # read temp
        user_option=input(f'Select Option {user_option_list}: ')

    )


if __name__ == '__main__':
    main()
