from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_form():

    delay = driver.find_element(By.ID, 'delay')

    delay.clear()

    delay.send_keys(45)

    driver.find_element(By.XPATH, "//*[text() = '7']").click()

    driver.find_element(By.XPATH, "//*[text() = '+']").click()

    driver.find_element(By.XPATH, "//*[text() = '8']").click()

    driver.find_element(By.XPATH, "//*[text() = '=']").click()

    result = WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//*[text() = '15']")))

    assert result.text == '15'

    driver.quit()
