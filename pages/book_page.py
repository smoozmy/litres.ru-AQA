import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Book_page(Base):

    # Locators

    pay_book_button = '//div[@data-testid="book-sale-block__price--button"]'


    # Getters

    def get_pay_book_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_book_button)))


    # Actions

    def click_pay_book_button(self):
        self.get_pay_book_button().click()


    # Methods

    def pay_book(self):
        self.click_pay_book_button()
        time.sleep(2)

