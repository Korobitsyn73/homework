class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def product_name(self):
        return self.name

    def product_price(self):
        return self.price

    def product_info(self):
        return f"Product: {self.name}, Price: {self.price}"
