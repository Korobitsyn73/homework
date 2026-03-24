from selenium.webdriver.common.by import By


class Login:
    '''
    Этот класс описывает шаги, вызываемые из теста test_shop.py, отвечающие за авторизацию
    пользователя на портале интернет-магазина.
    '''

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/ ")

    def login_entrance(self):
        '''
        Метод login_entrance вызывается из теста test_shop.py.
        Первым шагом: в окно авторизации вводится имя пользователя,
        вторым шагом: вводится пароль,
        третьим шагом: нажимается кнопка авторизации и выполняется вход на портал покупок.
        '''

        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')

        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

        self.driver.find_element(By.ID, 'login-button').click()
