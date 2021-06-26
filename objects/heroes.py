import datetime
import random
from .settings import crit_settings
from .items import Items

class Hero():
    ''' Hero of the game. Have gold and inventory'''

    def __init__(self, name):
        self.name = name
        self.birth = datetime.date.today()
        self.gold = 0
        self.inventory = Items()
        self.power = 10
        # self.location = 'Home'

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

    def go_farm(self, location):
        self.location = location
        location.add_hero(self)

    def return_from_farm(self):
        get_chance = random.randint(1,100)
        # Add base location
        self.location.remove_hero(self)
        if self.power >= self.location.power:
            crit_chance = crit_settings['base_crit_chance']
        else:
            crit_chance = (crit_settings['base_crit_chance'] *
                           (crit_settings['step_crit_chance'] * self.location.power // self.power))
        if get_chance <= crit_chance:
            return False
        return True

    def __repr__(self):
        return f'<Hero {self.name} with power {self.power}>'
        # def go home. Get random event from events
