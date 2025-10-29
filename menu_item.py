# menu_item.py

from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    @abstractmethod
    def calculate_total(self, quantity):
        pass


class MainCourse(MenuItem):
    def calculate_total(self, quantity):
        return self.get_price() * quantity


class Drink(MenuItem):
    # 10% discount on drinks if quantity > 3
    def calculate_total(self, quantity):
        total = self.get_price() * quantity
        if quantity > 3:
            total *= 0.9
        return total


class Dessert(MenuItem):
    # Flat ₹20 discount if order total > 300
    def calculate_total(self, quantity):
        total = self.get_price() * quantity
        if total > 300:
            total -= 20
        return total
