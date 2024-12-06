from selenium import webdriver

from pages.book_page import Book_page
from pages.favorite_page import Favorite_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_select_and_pay_book():
    driver = webdriver.Chrome()
    print('Start test')

    login = Login_page(driver)
    mp = Main_page(driver)
    bp = Book_page(driver)
    pp = Payment_page(driver)

    login.authorization()
    mp.search_book()
    bp.pay_book()
    pp.payment_finish()

    driver.quit()


def test_favorite_book():
    driver = webdriver.Chrome()
    print('Start test')

    login = Login_page(driver)
    mp = Main_page(driver)
    fp = Favorite_page(driver)

    login.authorization()
    mp.add_to_favorite_book()
    fp.remove_from_favorite()

    driver.quit()