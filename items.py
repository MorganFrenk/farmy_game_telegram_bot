import random
from .items import Items

class Item():
    '''Item in the game'''

    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price

    def __repr__(self):
        return f'<Item {self.name} with power {self.power}>'

class Items():
    '''List of game items. 
    Inventory, Shop, Loot'''

    def __init__(self):
        self.items = []

    def add_item(self, item):
        
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def find_item(self, name):
        '''Find item with power'''

        for item in self.items:
            if item.name == name:
                return item
        return False

    def list_items_with_power(self, power=False):
        '''List of all items with power'''
        
        items_with_power = []
        for item in self.items:
            if item.power <= power:
                items_with_power.append(item)
        return items_with_power

    def get_random_items(self, power=False, amount=1):
        '''Random item from all items or with power'''

        if power:
            random_items = self.list_items_with_power(power)
            return random.sample(random_items, amount)
        return random.sample(self.items, amount)