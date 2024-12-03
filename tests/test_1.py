import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from pages.main_page import Main_page


def test_select_book():
    driver = webdriver.Chrome()
    print('start test')

    login = Login_page(driver)
    mp = Main_page(driver)

    login.authorization()
    mp.search_book()

    driver.quit()
