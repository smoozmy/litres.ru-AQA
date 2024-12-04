import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.book_page import Book_page
from pages.favorite_page import Favorite_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_select_and_pay_book():
    driver = webdriver.Chrome()
    print('start test')

    login = Login_page(driver)
    mp = Main_page(driver)
    bp = Book_page(driver)

    login.authorization()
    mp.search_book()
    bp.pay_book()

    driver.quit()


def test_favorite_book():
    driver = webdriver.Chrome()
    print('start test')

    login = Login_page(driver)
    mp = Main_page(driver)
    fp = Favorite_page(driver)

    login.authorization()
    print('авторизация')
    mp.add_to_favorite_book()
    fp.remove_from_favorite()

    driver.quit()