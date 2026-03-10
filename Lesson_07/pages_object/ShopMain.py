from selenium.webdriver.common.by import By


class Main:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

        self.driver.find_element(By.ID, 'shopping_cart_container').click()
