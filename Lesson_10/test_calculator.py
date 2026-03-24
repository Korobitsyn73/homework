import allure
from selenium import webdriver
from pages_object.Calculator import Calculator


@allure.epic("Урок по отчётности в Allure")
@allure.severity("critical")
@allure.id("Slow calculator")
@allure.story("Тестирование работы медленного калькулятора")
@allure.feature("Арифметические действия")
@allure.title("Операция сложения")
@allure.description("Назначение времени ожидания в окне задержки и выполнение сложения чисел")
def test_slow_calc():
    browser = webdriver.Chrome()
    calculator = Calculator(browser)
    calculator.calc_start()
    calculator.adding_numbers()
