import datetime

# Time to farm from power
farm_times = {
    10: 20,
    20: 50
}

class Hero():
    ''' Hero of the game. Have gold and inventory'''

    def __init__(self, name):
        self.name = name
        self.birth = datetime.date.today()
        self.gold = 0
        self.inventory = []
        self.power = 0
    
    def add_gold(self, gold):
        self.gold += gold

    def add_item(self, item):
        self.inventory.append(item)
        # add power to hero from item

class Location():
    '''Location in the game'''

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.farm_time = farm_times[power]
        

class Item():
    '''Items in the game'''

    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price