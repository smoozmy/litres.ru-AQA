import random
import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class New_page(Base):

    # Locators

    genre = '//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/div/div[5]/a'
    format_text_checkbox = '//div[@data-testid="art__filters-art_types"][1]'
    subscription_switcher = '//div[@data-testid="filter_type--switcher"][1]'
    filter_book = '//a[@data-testid="art__title"][1]'

    # Getters

    def get_genre(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.genre)))

    def get_format_text_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.format_text_checkbox)))

    def get_subscription_switcher(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subscription_switcher)))

    def get_filter_book(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_book)))

        # Actions

    def click_genre(self):
        self.get_genre().click()

    def click_format_text_checkbox(self):
        self.get_format_text_checkbox().click()

    def click_subscription_switcher(self):
        self.get_subscription_switcher().click()

    def click_filter_book(self):
        self.get_filter_book().click()
        print("Клик по книге выполнен")


    # Methods

    def buy_filter_book(self):
        self.click_genre()
        print('Выбран жанр')
        time.sleep(2)
        self.click_format_text_checkbox()
        print('Выбран формат - текст')
        time.sleep(2)
        self.click_subscription_switcher()
        print('Выбран фильтр по подписке')
        time.sleep(2)
        self.click_filter_book()

        all_tabs = self.driver.window_handles
        print(f"Все открытые вкладки: {all_tabs}")
        self.driver.switch_to.window(all_tabs[-1])
        time.sleep(1)

        self.get_current_url()