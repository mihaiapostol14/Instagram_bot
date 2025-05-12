from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

class ElementChecker:
    def __init__(self, driver: WebDriver):
        """
        Initialize with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver object.
        """
        self.driver = driver

    def xpath_exists(self, xpath: str) -> bool:
        """
        Check if an element with the given XPath exists.

        Args:
            xpath (str): The XPath of the element.

        Returns:
            bool: True if exists, False otherwise.
        """
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    def id_exists(self, element_id: str) -> bool:
        """
        Check if an element with the given ID exists.

        Args:
            element_id (str): The ID of the element.

        Returns:
            bool: True if exists, False otherwise.
        """
        try:
            self.driver.find_element(By.ID, element_id)
            return True
        except NoSuchElementException:
            return False

    def class_exists(self, class_name: str) -> bool:
        """
        Check if an element with the given class name exists.

        Args:
            class_name (str): The class name of the element.

        Returns:
            bool: True if exists, False otherwise.
        """
        try:
            self.driver.find_element(By.CLASS_NAME, class_name)
            return True
        except NoSuchElementException:
            return False
        
    def tag_exists(self, tag_name):
        """Checks if an element with the given Tag exists on the page."""
        try:
            # Attempt to find the element by Tag
            self.driver.find_element(By.TAG_NAME, tag_name)
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