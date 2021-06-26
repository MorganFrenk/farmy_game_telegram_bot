import datetime
from .items import Items

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



