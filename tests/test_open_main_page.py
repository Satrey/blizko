from selenium import webdriver

def test_open_main_page():
    # Открытие главной страницы интернетмагазина 

    with webdriver.Chrome() as driver:
        
