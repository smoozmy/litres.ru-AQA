import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Favorite_page(Base):

    # Locators

    favorite_book_title = '//a[@data-testid="art__title"]'
    overlay_menu = '//*[@data-testid="overlay__trigger"]'
    remove_button = '//div[@role="button" and @aria-label="Убрать из отложенного"]'


    # Getters

    def get_favorite_book_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorite_book_title)))

    def get_overlay_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.overlay_menu)))

    def get_remove_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))


    # Actions

    def select_favorite_book_title(self):
        self.get_favorite_book_title().text

    def click_overlay_menu(self):
        self.get_overlay_menu().click()

    def click__remove_button(self):
        self.get_remove_button().click()

    # Methods

    def assert_book_title(self):
        assert  self.select_favorite_book_title() == 'Как тестируют в Google'

    def remove_from_favorite(self):
        self.click_overlay_menu()
        self.click__remove_button()
        print('Книга удалена из избранного ✅')
        time.sleep(1)
