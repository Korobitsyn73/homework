from selenium import webdriver
from pages_object.Calculator import Calculator


def test_slow_calc():
    browser = webdriver.Chrome()
    calculator = Calculator(browser)
    calculator.calc_start()
