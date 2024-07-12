from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, manufacturer, stock_quantity):
        self.__name = name
        self.__price = price
        self.__manufacturer = manufacturer
        self.__stock_quantity = stock_quantity
        
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_manufacturer(self):
        return self.__manufacturer
    def get_stock_quantity(self):
        return self.__stock_quantity
    
    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price
    def set_stock_quantity(self, quantity):
        self.__stock_quantity = quantity
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    
class Phone(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, screen_size, camera_resolution):
        super().__init__(name, price, manufacturer, stock_quantity)
        self.screen_size = screen_size
        self.camera_resolution = camera_resolution
        
class Laptop(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, processor, ram, storage):
        super().__init__(name, price, manufacturer, stock_quantity)
        self.processor = processor
        self.ram = ram
        self.storage = storage
        
class TV(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, screen_size, resolution):
        super().__init__(name, price, manufacturer, stock_quantity)
        self.screen_size = screen_size
        self.resolution = resolution


class Order():
    def __init__(self, customer_info):
        self.customer_info = customer_info
        self.items = {}
    
    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Khach hang chua them san pham")
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def calculate_total(self):
        return sum(product.get_price() * quantity for product, quantity in self.items.items())
    
    def generate_invoice(self):
        print("Thông tin khách hàng :")
        for key, value in self.customer_info.items():
            print(f"{key}: {value}",end = "")
            
        print("\nOrder:")
        for product, quantity in self.items.items():
            print(f"{product.get_name()} - Quantity: {quantity} - Price: ${product.get_price() * quantity}")
        print(f"Total: ${self.calculate_total()}")
    
if __name__ == "__main__":
    customer_info = {"Name": "Jek", " - Address": "HaNoi", " - Phone": "84+12345789"}
    order = Order(customer_info)

    phone = Phone("iPhone 12", 999, "Apple", 100, 6.1, "12MP")
    laptop = Laptop("MacBook Pro", 1999, "Apple", 50, "M1", 16, 512)

    order.add_item(phone, 1)
    order.add_item(laptop, 1)

    order.generate_invoice()
        
        

        
    
