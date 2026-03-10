from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def cart_checkout(self):

        self.driver.find_element(By.ID, 'checkout').click()
