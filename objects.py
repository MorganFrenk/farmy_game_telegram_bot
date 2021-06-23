import datetime
import random


# Farm time from power
farm_times = {
    10: 20,
    20: 50
}

# Gold from power
location_reward = {
    10: 50,
    20: 100,
}

hero_statuses = {
    'wounded',
    'In location',
    
}


class Hero():
    ''' Hero of the game. Have gold and inventory'''

    def __init__(self, name):
        self.name = name
        self.birth = datetime.date.today()
        self.gold = 0
        self.inventory = Items()
        self.power = 0
        self.location = 'Home'

    def rename(self, name):
        self.name = name

    def add_power(self, power):
        self.power += power

    def add_gold(self, gold):
        self.gold += gold

    def add_item(self, item):
        self.inventory.add_item(item)
        self.power += item.power

    def remove_item(self, item):
        self.inventory.remove_item(item)
        self.power -= item.power

    def farm(self, location):
        self.location = location
        location.add_hero(self)

    def __repr__(self):
        return f'<Hero {self.name} with power {self.power}>'
    #def go home. Get random event from events


class Location():
    '''Location in the game'''

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.farm_time = farm_times[power]
        self.reward = location_reward[power]
        self.loot_pool = Items.list_items_with_power(self.power)
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def refull_loot_pool(self):
        self.loot_pool = Items.list_items_with_power(self.power)

    def get_loot(self):
        return self.loot_pool.get_random_items(self.power)

    def __repr__(self):
        return f'<Location {self.name} with power {self.power}>'


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

 
# Do i need this class?
class Shop():

    def __init__(self, power):
        self.items = Items.list_items_with_power(power)

    def refull_shop(self, power):
        self.items = Items.list_items_with_power(power)

    
# add events

