from selenium.webdriver.common.by import By


class Cart:
    '''
    Этот класс описывает шаг, вызываемый из теста test_shop.py -
    нажатие кнопки checkout.
    '''

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def cart_checkout(self):
        """
        Метод cart_checkout вызывается из теста test_shop.py
        и осуществляет нажатие кнопки checkout.
        """
        self.driver.find_element(By.ID, 'checkout').click()
