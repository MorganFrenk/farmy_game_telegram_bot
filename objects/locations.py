from .settings import farm_time_from_power, reward_from_power
from .items import Items


class Location():

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.farm_time = farm_time_from_power[power]
        self.reward = reward_from_power[power]
        self.loot_pool = Items.list_items_with_power(self.power)
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def refull_loot_pool(self):
        self.loot_pool = Items.list_items_with_power(self.power)

    def get_loot(self):
        return self.loot_pool.get_random_items(self.power)

    def __repr__(self):
        return f'<Location {self.name} with power {self.power}>'


class Locations():

    def __init__(self):
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)
