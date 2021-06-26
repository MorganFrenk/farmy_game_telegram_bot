from .settings import farm_time_from_power, reward_from_power, item_settings
from .items import all_game_items


class Location():
    '''Location of the game. Dungeons for looting.
    Have reward, power level, random loot pool and define farm time'''

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.farm_time = farm_time_from_power[power]
        self.reward = reward_from_power[power]
        self.loot_pool = all_game_items.get_random_items(self.power, item_settings['loot_pool_size'])
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def refill_loot_pool(self):
        '''Get random loot for the location'''

        self.loot_pool = all_game_items.get_random_items(self.power, item_settings['loot_pool_size'])

    def get_loot(self):
        return self.loot_pool.get_random_items(self.power)

    def __repr__(self):
        return f'<Location {self.name} with power {self.power}>'


class Locations():
    '''List of locations.'''

    def __init__(self):
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)
