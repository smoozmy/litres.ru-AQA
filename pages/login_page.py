import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):

    BASE_URL = 'https://www.litres.ru/'

    TEST_USER = 'smoozmy@gmail.com'
    PASSWORD = 'smoozmytest'


    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    # Locators

    user_button = '//*[@id="layout-root"]/header/div[2]/nav/div[3]/div[2]'
    email_textfield = '//input[@id="auth__input--enterEmailOrLogin"]'
    login_one_button = '//*[@id="modal"]/div/div/div/div/div/div/div/form/div[3]/button'
    password_textfield = '//*[@id="modal"]/div/div/div/div/div/div/div/form/div[2]/div/div/input'
    login_two_button = '//*[@id="modal"]/div/div/div/div/div/div/div/form/div[3]/button/div/div/div'
    profile_word = '//*[@id="layout-root"]/header/div[2]/nav/div[3]/div[2]/div/a/div[2]'

    # Getters

    def get_user_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_button)))

    def get_email_textfield(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_textfield)))

    def get_login_one_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_one_button)))

    def get_password_textfield(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_textfield)))

    def get_login_two_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_two_button)))

    def get_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_word)))


    # Actions

    def click_user_button(self):
        self.get_user_button().click()

    def input_email_textfield(self, email):
        self.get_email_textfield().send_keys(email)

    def click_login_one_button(self):
        self.get_login_one_button().click()

    def input_password_textfield(self, password):
        self.get_password_textfield().send_keys(password)

    def click_login_two_button(self):
        self.get_login_two_button().click()



    # Methods

    def authorization(self):
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.get_current_url()

        self.click_user_button()
        self.input_email_textfield(self.TEST_USER)
        self.click_login_one_button()
        time.sleep(1)
        self.input_password_textfield(self.PASSWORD)
        self.click_login_two_button()

        self.assert_word(self.get_profile_word(), 'Профиль')
        print(f'Выполнена авторизация пользователем {self.TEST_USER}')
