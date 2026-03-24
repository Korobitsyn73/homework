from selenium.webdriver.common.by import By


class Main:
    '''
    Этот класс описывает шаги, вызываемые из теста test_shop.py, отвечающие за выбор товара
    на портале интернет-магазина, добавление его в корзину и переход в корзину.
    '''

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        '''
        Метод add_to_cart вызывается из теста test_shop.py.
        Три шага: последовательно добавляют в корзину товары, четвёртым - осуществляется
        переход в корзину.

        '''

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

        self.driver.find_element(By.ID, 'shopping_cart_container').click()
