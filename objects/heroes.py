import datetime
import random
from .settings import crit_settings, item_settings
from .items import Items
from .locations import location_home


class Hero():
    ''' Hero of the game. Have power, gold, inventory and status'''

    def __init__(self, name):
        self.name = name
        self.birth = datetime.date.today()
        self.gold = 0
        self.inventory = Items()
        self.power = 10
        self.status = 'ready'
        self.location = location_home

    def rename(self, name):
        self.name = name

    def add_power(self, power):
        self.power += power

    def remove_power(self, power):
        self.power -= power

    def add_gold(self, gold):
        self.gold += gold

    def remove_gold(self, gold):
        self.gold -= gold

    def add_item(self, item):
        self.inventory.add_item(item)
        self.add_power(item.power)

    def remove_item(self, item):
        self.inventory.remove_item(item)
        self.remove_power(item.power)

    def go_farm(self, location):
        '''Set location to go. Change status'''

        self.location = location
        self.status = 'farm'
        location.add_hero(self)

    def return_from_farm(self):
        '''Get the farm result from random chance (fail or success).
        Get random loot.'''

        get_crit_result = random.randint(1,100)
        get_item_result = random.randint(1,100)

        if self.power >= self.location.power:
            crit_chance = crit_settings['base_crit_chance']
            item_chance = item_settings['base_item_chance']
        else:
            crit_chance = (crit_settings['base_crit_chance'] *
                           (crit_settings['step_crit_chance'] * self.location.power // self.power))
            item_chance = (crit_settings['base_item_chance'] *
                           (crit_settings['step_item_chance'] * self.location.power // self.power))

        if get_crit_result <= crit_chance:
            self.status = 'wounded'
            return False

        if get_item_result <= item_chance:
            self.add_item(self.location.loot_pool.get_random_items(power=self.location.power))

        self.add_gold(self.location.reward)
        self.status = 'ready'
        self.location.remove_hero(self)
        # Hero location to home location
        return True

    def __repr__(self):
        return f'<Hero {self.name} with power {self.power}>'
