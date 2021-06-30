import random
from .settings import power_setting


class Item():
    '''Item in the game with price and power'''

    def __init__(self, name, power, price) -> None:
        self.name = name
        self.power = power
        self.price = price

    def __repr__(self):
        return f'<Item {self.name} with power {self.power}>'


class Items():
    '''List of game items.
    For: inventory, location loot'''

    def __init__(self):
        self.items = []

    def add_item(self, items):
        '''Add item. Items can be list or object'''

        if isinstance(items, list):
            self.items.extend(items)
        else:
            self.items.append(items)

    def remove_item(self, items):
        '''Remove item. Items can be list or object'''

        if items in self.items:
            if isinstance(items, list):
                self.items = list(set(self.items) - set(items))
            else:
                self.items.remove(items)

    def find_item(self, name):
        '''Find item with name'''

        for item in self.items:
            if item.name == name:
                return item
        return False

    def list_items_with_power(self, power, power_limit=False):
        '''List of all items with maximum power of "power" and minimum "power_limit"
        If power limit is not set, search throughout one power level'''

        if not power_limit:
            for lev in range(1, power_setting['max_power_level']):
                lev_pow = power_setting['base_power'] * power_setting['step_power'] ** lev
                if lev == 1:
                    prev_lev_pow = 0
                if power < lev_pow:
                    power_limit = prev_lev_pow
                    break
                prev_lev_pow = lev_pow

        items_with_power = []
        for item in self.items:
            if (item.power <= power and item.power >= power_limit):
                items_with_power.append(item)
        return items_with_power

    def get_random_items(self, power=False, power_limit=False, amount=1):
        '''Random items or random items with certain power and mininum power limit'''

        if power:
            random_items = self.list_items_with_power(power, power_limit=power_limit)
            return random.sample(random_items, amount)
        return random.sample(self.items, amount)


# Game objects
all_game_items = Items()

item_1 = Item('item', 10, 200)
item_2 = Item('item', 10, 200)
item_3 = Item('item', 10, 200)
item_4 = Item('item', 10, 200)
item_5 = Item('item', 10, 200)

item_6 = Item('item', 20, 200)
item_7 = Item('item', 20, 200)
item_8 = Item('item', 20, 200)
item_9 = Item('item', 20, 200)

item_10 = Item('item', 30, 300)
item_11 = Item('item', 30, 300)
item_12 = Item('item', 30, 300)

item_13 = Item('item', 40, 300)
item_14 = Item('item', 40, 300)

item_15 = Item('item', 50, 300)


all_game_items.add_item([item_1, item_2, item_3, item_4, item_5,
                                 item_6, item_7, item_8, item_9, item_10,
                                 item_11, item_12, item_13, item_14, item_15])


class Shop(Items):
    '''Special class for the game shop'''

    def refill_shop(self, items_pool=all_game_items):
        '''Fill shop with random items. Loop through all power levels.
        Get the amount of items with define power from: max level
        minus current level '''

        for level in range(1, power_setting['max_power_level']):
            items_to_add = items_pool.get_random_items(
                power=(power_setting['base_power'] * power_setting['step_power'] ** level - 1),
                amount=power_setting['max_power_level'] - level)
            self.items.extend(items_to_add)
