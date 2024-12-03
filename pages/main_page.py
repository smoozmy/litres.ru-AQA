import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    # Locators
    search = '//*[@id="layout-root"]/header/div[2]/div[2]/div/div/form/div/input'
    search_button = '//*[@id="layout-root"]/header/div[2]/div[2]/div/div/form/div/button[2]'
    find_book = '//*[@id="main"]/div/div[4]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[1]/a[1]/p'


    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_find_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.find_book)))


    # Actions

    def input_search(self):
        self.get_search().send_keys('Как тестируют в Google')

    def click_search_button(self):
        self.get_search_button().click()

    def click_find_book(self):
        self.get_find_book().click()




    # Methods

    def search_book(self):
        self.input_search()
        self.click_search_button()
        time.sleep(1)
        print('Выполнен поиск по книге')

        self.click_find_book()

        all_tabs = self.driver.window_handles
        print(f"Все открытые вкладки: {all_tabs}")

        self.driver.switch_to.window(all_tabs[-1])
        time.sleep(1)
        self.get_current_url()

        assert WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="book-card__wrapper"]/div[2]/div[3]/div[1]/h1'))).text == 'Как тестируют в Google'



