from selenium.webdriver.common.by import By


class Order:
    """
    Этот класс описывает шаги, вызываемые из теста test_shop.py,
    отвечающие за оформление заказа.

    """

    def __init__(self, driver):
        self.driver = driver

    def order_sum(self):
        """
        Метод order_sum вызывается из теста test_shop.py.
        Первым шагом: в окно авторизации вводится имя пользователя,
        вторым шагом: вводится фамилия,
        третьим шагом: вводится почтовый индекс
        четвёртым шагом: нажимается кнопка Continue для просмотра данных и суммы заказа.
        Сумма заказа возвращается в строковом выражении, в формате текста, сохраняется в переменную total
        и выносится в консоль.
        Выполняется проверка соответствия суммы ожидаемому результату.
        """

        self.driver.find_element(By.ID, 'first-name').send_keys('Maksim')

        self.driver.find_element(By.ID, 'last-name').send_keys('Korobitsyn')

        self.driver.find_element(By.ID, 'postal-code').send_keys('450083')

        self.driver.find_element(By.ID, 'continue').click()

        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

        assert total == 'Total: $58.29'

        print(total)

        self.driver.quit()
