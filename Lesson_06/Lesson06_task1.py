from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get('http://uitestingplayground.com/ajax')
blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

green_banner = driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text

print(green_banner)


driver.quit()
