import datetime
from .additionals import farm_times, location_reward
from .items import Items

class Location():

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

# Do i need this class?
class Shop():
    '''Shop in the game'''

    def __init__(self, power):
        self.items = Items.list_items_with_power(power)

    def refull_shop(self, power):
        self.items = Items.list_items_with_power(power)

    
# add events