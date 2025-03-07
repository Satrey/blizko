from pages.main_page import MainPage


def test_open_main_page(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()


def test_user_autentification(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.autentification()


def test_main_menu(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.go_to_main_menu()


def test_cart_button(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.go_to_cart()


def test_search_field(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.send_search_text()
