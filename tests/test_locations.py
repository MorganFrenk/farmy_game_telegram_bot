import unittest
from objects.locations import Location
from objects.items import Items, Item
from objects.heroes import Hero


class TestItems(unittest.TestCase):

    def setUp(self) -> None:
        self.items_pool = Items()
        self.item_1 = Item('item', 19, 200)
        self.item_2 = Item('item', 39, 200)
        self.item_3 = Item('item', 79, 200)
        self.item_4 = Item('item', 159, 200)
        self.item_5 = Item('item', 319, 200)
        self.items_pool.add_item([self.item_1, self.item_2, self.item_3, self.item_4, self.item_5])
        self.test_location = Location('test loc', 19, self.items_pool, pool_amount=1)
        