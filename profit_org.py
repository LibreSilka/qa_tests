import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    """Инициализация WebDriver"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@allure.feature("Navigation Bar")
@allure.story("Проверка вкладок в шапке сайта")
@allure.title("Проверка переходов по вкладкам в шапке сайта")
def test_navigation_tabs(driver):
    """Тест перехода по вкладкам в шапке сайта"""
    with allure.step("Открытие главной страницы"):
        driver.get("https://profit.org.ru/")

    # Список вкладок в шапке сайта
    tabs = [
        {"name": "Услуги", "locator": "//a[text()='Услуги']"},
        {"name": "Портфолио", "locator": "//a[text()='Портфолио']"},
        {"name": "Вакансии", "locator": "//a[text()='Вакансии']"},
        {"name": "Контакты", "locator": "//a[text()='Контакты']"},
    ]

    for tab in tabs:
        with allure.step(f"Переход на вкладку {tab['name']}"):
            # Клик по вкладке
            tab_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, tab["locator"]))
            )
            tab_element.click()

            # Проверка, что вкладка загружается
            assert driver.current_url != "https://profit.org.ru/", f"Вкладка {tab['name']} не открылась"

            # Логирование перехода
            print(f"Успешно перешли на вкладку: {tab['name']}")