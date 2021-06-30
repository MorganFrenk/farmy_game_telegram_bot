from .settings import farm_time_from_power, reward_from_power, item_settings
from .items import Items, all_game_items


class Location():
    '''Location of the game. Dungeons for looting.
    Have reward, power level, random loot pool and define farm time'''

    def __init__(self, name: str, power: int, items_pool, pool_amount=item_settings['loot_pool_size']):
        self.name = name
        self.power = power
        self.farm_time = farm_time_from_power[power]
        self.reward = reward_from_power[power]
        self.loot_pool = items_pool.get_random_items(self.power, amount=pool_amount)
        self.heroes = []

    def add_hero(self, hero):
        if hero not in self.heroes:
            self.heroes.append(hero)

    def remove_hero(self, hero):
        if hero in self.heroes:
            self.heroes.remove(hero)

    def refill_loot_pool(self, items_pool, pool_amount=item_settings['loot_pool_size']):
        '''Get random loot with a define amount for the location from any Items object'''

        self.loot_pool = items_pool.get_random_items(self.power, pool_amount)

    def __repr__(self):
        return f'<Location {self.name} with power {self.power}>'


class Locations():
    '''List of locations.'''

    def __init__(self):
        self.locations = []

    def add_location(self, location):
        if location not in self.locations:
            self.locations.append(location)

    def remove_location(self, location):
        if location in self.locations:
            self.locations.remove(location)
