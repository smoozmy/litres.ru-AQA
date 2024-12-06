import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Profile_page(Base):

    # Locators

    profile_main = '//*[@id="main"]/div/nav/ul/li[1]/a'
    profile_secure = '//*[@id="main"]/div/nav/ul/li[2]/a'
    profile_payment = '//*[@id="main"]/div/nav/ul/li[3]/a'
    profile_promo = '//*[@id="main"]/div/nav/ul/li[4]/a'
    profile_notifications = '//*[@id="main"]/div/nav/ul/li[5]/a'
    profile_help = '//*[@id="main"]/div/nav/ul/li[6]/a'
    profile_logout = '//*[@id="main"]/div/nav/ul/li[7]/button'
    logout_button = '//*[@id="modal"]/div[2]/div/div/div/div/div[3]/button[1]/div/div'

    # Getters

    def get_profile_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_main)))

    def get_profile_secure(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_secure)))

    def get_profile_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_payment)))

    def get_profile_promo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_promo)))

    def get_profile_notifications(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_notifications)))

    def get_profile_help(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_help)))

    def get_profile_logout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_logout)))

    def get_logout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logout_button)))

    # Actions

    def click_profile_main(self):
        self.get_profile_main().click()

    def click_profile_secure(self):
        self.get_profile_secure().click()

    def click_profile_payment(self):
        self.get_profile_payment().click()

    def click_profile_promo(self):
        self.get_profile_promo().click()

    def click_profile_notifications(self):
        self.get_profile_notifications().click()

    def click_profile_help(self):
        self.get_profile_help().click()

    def click_profile_logout(self):
        self.get_profile_logout().click()

    def click_logout_button(self):
        self.get_logout_button().click()

    # Methods

    def check_sections(self):
        self.click_profile_secure()
        time.sleep(1)
        self.click_profile_payment()
        time.sleep(1)
        self.click_profile_promo()
        time.sleep(1)
        self.click_profile_notifications()
        time.sleep(1)
        self.click_profile_help()
        time.sleep(1)
        self.click_profile_main()
        time.sleep(1)
        print('Выполнен переход по всем секциям раздела Профиль ✅')

    def logout(self):
        self.click_profile_logout()
        time.sleep(1)
        self.click_logout_button()
        time.sleep(1)

        print('Пользователь разлогинен ✅')



