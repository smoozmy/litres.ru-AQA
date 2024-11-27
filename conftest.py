# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from utilites.config import BASE_URL
#
#
# @pytest.fixture(scope='session')
# def browser():
#     options = Options()
#     options.add_argument('--incognito')
#     driver = webdriver.Chrome(options=options)
#
#     driver.get(BASE_URL)
#     yield driver
#
#     driver.quit()