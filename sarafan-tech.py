import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации WebDriver"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@allure.feature("Sarafan Website")
@allure.story("Acceptance of Private Policy")
@allure.title("Тест кнопки 'Got it' на странице 'Technology'")
@allure.description("Проверка кликабельности кнопки 'Got it' после скроллинга на странице 'Technology'.")
def test_got_it_button(driver):
    """Проверка кликабельности кнопки 'Got it'"""
    with allure.step("Открытие главной страницы"):
        driver.get("https://sarafan.tech/")

    with allure.step("Ожидание загрузки главной страницы"):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

    with allure.step("Переход на вкладку 'Technology'"):
        technology_tab = driver.find_element(By.LINK_TEXT, "Technology")
        technology_tab.click()

    with allure.step("Ожидание появления уведомления 'Privacy policy'"):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Privacy policy']"))
        )

    with allure.step("Скроллинг страницы"):
        driver.execute_script("window.scrollBy(0, 300);")

    with allure.step("Нажатие на кнопку 'Got it'"):
        got_it_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Got it']"))
        )
        got_it_button.click()

    with allure.step("Проверка наличия контента 'Recognition categories'"):
        recognition_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Recognition categories']"))
        )
        assert recognition_content, "Контент 'Recognition categories' не отображается."

