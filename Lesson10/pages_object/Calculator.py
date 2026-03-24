import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """
    Этот класс описывает шаги, вызываемые из теста test_calculator.py, для проверки медленного калькулятора,
    в котором есть возможность выставить желаемое время задержки выполнения арифметических действий.
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Назначить время ожидания в поле задержки")
    def calc_start(self):
        """
        Метод calc_ctart вызывается из теста test_calculator.py.
        Первым шагом: находит по id окно задержки delay,
        вторым шагом: очищает его от старых данных,
        третьим шагом: назначает желаемое значение задержки(времени ожидания)
        """
        delay_act = self.driver.find_element(By.ID, 'delay')
        delay_act.clear()
        delay_act.send_keys(45)

    @allure.step("Выполнить сложение чисел")
    def adding_numbers(self):
        """
        Метод adding_numbers вызывается из теста test_calculator.py.
        Он выполняет сложение чисел 7 и 8, по истечении времени задержки, получает результат
        и сверяет его с ожидаемым.
        Результат возвращается в строковом выражении, в формате текста и сохраняется в переменную result.
        """
        self.driver.find_element(By.XPATH, "//*[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '=']").click()

        result = WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//*[text() = '15']")))

        assert result.text == '15'

        self.driver.quit()
