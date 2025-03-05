import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    """Класс главной страницы"""

    # Данные

    main_page_url = "https://tyumen.blizko.ru/"

    # Локаторы

    pass_locator = "EC.element_to_be_clickable((By.ID, self.password)"

    # Действия

    # Методы
