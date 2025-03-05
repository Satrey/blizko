from selenium import webdriver

from pages.main_page import MainPage


def test_open_main_page():
    # Открытие главной страницы интернетмагазина

    with webdriver.Chrome() as driver:
        mp = MainPage(driver)
        mp.go_to_base_url()
