from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def calc_start(self):

        delay_act = self.driver.find_element(By.ID, 'delay')
        delay_act.clear()
        delay_act.send_keys(45)

        self.driver.find_element(By.XPATH, "//*[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//*[text() = '=']").click()

        result = WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//*[text() = '15']")))

        assert result.text == '15'

        self.driver.quit()
