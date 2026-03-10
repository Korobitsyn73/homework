from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get('http://the-internet.herokuapp.com/login')


user_name = driver.find_element(By.CSS_SELECTOR, "#username")

user_name.send_keys("tomsmith")

sleep(3)

parole = driver.find_element(By.CSS_SELECTOR, "#password")

parole.send_keys("SuperSecretPassword!")

sleep(3)


login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

login.click()

sleep(3)

green_banner = driver.find_element(By.CSS_SELECTOR, '#flash')

print(green_banner.text)


driver.quit()
