from selenium.webdriver.common.by import By


class Order:

    def __init__(self, driver):
        self.driver = driver

    def order_sum(self):

        self.driver.find_element(By.ID, 'first-name').send_keys('Maksim')

        self.driver.find_element(By.ID, 'last-name').send_keys('Korobitsyn')

        self.driver.find_element(By.ID, 'postal-code').send_keys('450083')

        self.driver.find_element(By.ID, 'continue').click()

        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

        assert total == 'Total: $58.29'

        print(total)

        self.driver.quit()
