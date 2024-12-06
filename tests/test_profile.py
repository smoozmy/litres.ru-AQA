from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.profile_page import Profile_page


def test_profile_check():
    driver = webdriver.Chrome()
    print('Start test')

    lp = Login_page(driver)
    mp = Main_page(driver)
    pp = Profile_page(driver)

    lp.authorization()
    mp.go_to_profile()
    pp.check_sections()

    driver.quit()

def test_logout():
    driver = webdriver.Chrome()
    print('Start test')

    lp = Login_page(driver)
    mp = Main_page(driver)
    pp = Profile_page(driver)

    lp.authorization()
    mp.go_to_profile()
    pp.logout()

    driver.quit()
