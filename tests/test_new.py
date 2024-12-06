from selenium import webdriver

from pages.book_page import Book_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.new_page import New_page
from pages.payment_page import Payment_page


def test_new_book_with_filter():
    driver = webdriver.Chrome()

    lp = Login_page(driver)
    mp = Main_page(driver)
    np = New_page(driver)
    bp = Book_page(driver)

    lp.authorization()
    mp.go_to_new()
    np.buy_filter_book()

    driver.quit()


