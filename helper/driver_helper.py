from selenium.webdriver.remote.webdriver import WebDriver


class DriverHelper:
    def __init__(self, driver: WebDriver):
        """
        Initialize with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver object.
        """
        self.driver = driver

    def send_by_url(self, url):
        """
        Navigates to the specified URL using the web driver.

        Args:
            url (str): The URL to navigate to.

        Raises:
            WebDriverException: If there is an issue with navigating to the URL.
        """
        # Use the web driver to open the specified URL
        self.driver.get(url=url)


    def close_driver(self):
        """Close the WebDriver instance and quits the browser.

        This method closes the current window and terminates the WebDriver session.
        """
        self.driver.close()  # Close the current window
        self.driver.quit()  # Quit the WebDriver session and close all associated windows
