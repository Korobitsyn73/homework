from selenium import webdriver
from pages_object.ShopLogin import Login
from pages_object.ShopMain import Main
from pages_object.ShopCart import Cart
from pages_object.ShopOrder import Order


def test_entrance():

    browser = webdriver.Firefox()

    entrance = Login(browser)
    entrance.login_entrance()

    added = Main(browser)
    added.add_to_cart()

    checkout = Cart(browser)
    checkout.cart_checkout()

    ordering = Order(browser)
    ordering.order_sum()
