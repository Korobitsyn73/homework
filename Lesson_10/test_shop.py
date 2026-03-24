import allure
from selenium import webdriver
from pages_object.ShopLogin import Login
from pages_object.ShopMain import Main
from pages_object.ShopCart import Cart
from pages_object.ShopOrder import Order


@allure.epic("Урок по отчётности в Allure")
@allure.severity("critical")
@allure.id("Интернет-магазин")
@allure.story("Авторизация и покупка")
@allure.feature("Тестирование работы интернет-магазина")
@allure.title("Действия на портале магазина")
@allure.description("Добавление товаров в корзину и проверка итоговой стоимости")
def test_entrance():

    browser = webdriver.Firefox()
    with allure.step("Авторизоваться в интернет-магазине"):
        entrance = Login(browser)
        entrance.login_entrance()

    with allure.step("Добавить в корзину товары, перейти в корзину"):
        added = Main(browser)
        added.add_to_cart()

    with allure.step("Нажать кнопку checkout"):
        checkout = Cart(browser)
        checkout.cart_checkout()

    with allure.step("Оформить заказ и проверить сумму"):
        ordering = Order(browser)
        ordering.order_sum()
