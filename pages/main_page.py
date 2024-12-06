import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):

    # Locators
    search = '//input[@data-testid="search__input"]'
    search_button = '//button[@data-testid="search__button"]'
    search_result_book = '//img[@data-testid="adaptiveCover__img"][1]'


    favorite_button = '//div[@data-testid="tab-favorite"]'
    postpone_search_result_book = '//button[@data-testid="art__postponeButton--unLiked"][1]'

    user_button = '//div[@data-testid="user-button"]'


    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_search_result_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_result_book)))

    def get_favorite_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorite_button)))

    def get_postpone_search_result_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postpone_search_result_book)))

    def get_user_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_button)))


    # Actions

    def input_search(self):
        self.get_search().send_keys('Как тестируют в Google')

    def click_search_button(self):
        self.get_search_button().click()

    def click_search_result_book(self):
        self.get_search_result_book().click()

    def click_favorite_button(self):
        self.get_favorite_button().click()

    def click_postpone_search_result_book(self):
        self.get_postpone_search_result_book().click()

    def click_user_button(self):
        self.get_user_button().click()


    # Methods

    def search_book(self):
        self.input_search()
        self.click_search_button()
        time.sleep(1)
        print('Выполнен поиск по книге')

        self.click_search_result_book()

        all_tabs = self.driver.window_handles
        print(f"Все открытые вкладки: {all_tabs}")

        self.driver.switch_to.window(all_tabs[-1])
        time.sleep(1)
        self.get_current_url()

        assert WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="book-card__wrapper"]/div[2]/div[3]/div[1]/h1'))).text == 'Как тестируют в Google'


    def add_to_favorite_book(self):
        self.input_search()
        self.click_search_button()
        time.sleep(1)
        print('Выполнен поиск по книге')

        self.click_postpone_search_result_book()
        self.click_favorite_button()
        print('Книга добавлена в ибранное ✅')
        time.sleep(2)
        self.get_current_url()

    def go_to_profile(self):
        self.click_user_button()
        time.sleep(1)
        self.get_current_url()
        print('Выполнен перехорд в Профиль')




