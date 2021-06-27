import random
from .settings import power_setting


class Item():
    '''Item in the game with price and power'''

    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price

    def __repr__(self):
        return f'<Item {self.name} with power {self.power}>'


class Items():
    '''List of game items.
    For: inventory, shop, location loot'''

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def find_item(self, name):
        '''Find item with name'''

        for item in self.items:
            if item.name == name:
                return item
        return False

    def list_items_with_power(self, power):
        '''List of all items with power'''

        items_with_power = []
        for item in self.items:
            if item.power <= power:
                items_with_power.append(item)
        return items_with_power

    def get_random_items(self, power=False, amount=1):
        '''Random items or random items with certain power.'''

        if power:
            random_items = self.list_items_with_power(power)
            return random.sample(random_items, amount)
        return random.sample(self.items, amount)


class Shop(Items):
    '''Special class for the game shop'''

    def refill_shop(self, items_pool):
        '''Fill shop with random items. Loop through all power levels.
        Get the amount of items with define power from max level
        minus current level '''

        for level in range(power_setting['max_power']):
            items_to_add = items_pool.get_random_items(
                power=(power_setting['base_power'] + power_setting['step_power'] * level),
                amount=power_setting['max_power_level'] - level)
            self.items.extend(items_to_add)


all_game_items = Items()
