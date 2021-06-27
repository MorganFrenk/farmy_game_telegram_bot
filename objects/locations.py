from .settings import farm_time_from_power, reward_from_power, item_settings


class Location():
    '''Location of the game. Dungeons for looting.
    Have reward, power level, random loot pool and define farm time'''

    def __init__(self, name: str, power: int, items):
        self.name = name
        self.power = power
        self.farm_time = farm_time_from_power[power]
        self.reward = reward_from_power[power]
        self.loot_pool = items.get_random_items(self.power, item_settings['loot_pool_size'])
        self.heroes = []

    def add_hero(self, hero):
        if hero not in self.heroes:
            self.heroes.append(hero)

    def remove_hero(self, hero):
        if hero in self.heroes:
            self.heroes.remove(hero)

    def refill_loot_pool(self, items_pool):
        '''Get random loot for the location from any Items object'''

        self.loot_pool = items_pool.get_random_items(self.power, item_settings['loot_pool_size'])

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


location_home = Location('Home', 0)
