import unittest
from objects.items import Items, Item, Shop


class TestItems(unittest.TestCase):

    def setUp(self) -> None:
        self.item_1 = Item('item one', 1, 100)
        self.item_2 = Item('item two', 2, 200)
        self.items_pool = Items()

    def test_add_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertIn(self.item_1, self.items_pool.items)

    def test_remove_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.items_pool.remove_item(self.item_1)
        self.assertNotIn(self.item_1, self.items_pool.items)

    def test_add_multiple_items(self) -> None:
        self.items_pool.add_item([self.item_1, self.item_2])
        self.assertIn(self.item_1 and self.item_2, self.items_pool.items)

    def test_find_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertEqual(self.item_1, self.items_pool.find_item(self.item_1.name))

    def test_list_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.items_pool.add_item(self.item_2)
        self.assertIn(self.item_1, self.items_pool.list_items_with_power(self.item_1.power))

        self.assertIn(self.item_1 and self.item_2, self.items_pool.list_items_with_power(self.item_2.power))

        self.assertIn(self.item_1 and self.item_2,
                      self.items_pool.list_items_with_power(10, power_limit=self.item_1.power))
        self.assertIn(self.item_2,
                      self.items_pool.list_items_with_power(10, power_limit=self.item_2.power))

    def test_random_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertIn(self.item_1, self.items_pool.get_random_items())

        self.items_pool.add_item(self.item_2)
        self.assertIn(self.item_1 and self.item_2, self.items_pool.get_random_items(amount=2))

        self.assertIn(self.item_1, self.items_pool.get_random_items(power=1))

        self.assertIn(self.item_1 and self.item_2, self.items_pool.get_random_items(power=2, amount=2))

    def test_shop_refill(self) -> None:
        shop = Shop()
        self.item_1 = Item('item', 4, 200)
        self.item_2 = Item('item', 5, 200)
        self.item_3 = Item('item', 6, 200)
        self.item_4 = Item('item', 7, 200)
        self.item_5 = Item('item', 8, 200)

        self.item_6 = Item('item', 16, 200)
        self.item_7 = Item('item', 17, 200)
        self.item_8 = Item('item', 18, 200)
        self.item_9 = Item('item', 19, 200)

        self.item_10 = Item('item', 27, 300)
        self.item_11 = Item('item', 28, 300)
        self.item_12 = Item('item', 29, 300)

        self.item_13 = Item('item', 38, 300)
        self.item_14 = Item('item', 39, 300)

        self.item_15 = Item('item', 49, 300)

        self.items_pool.add_item([self.item_1, self.item_2, self.item_3, self.item_4, self.item_5,
                                 self.item_6, self.item_7, self.item_8, self.item_9, self.item_10,
                                 self.item_11, self.item_12, self.item_13, self.item_14, self.item_15])

        shop.refill_shop(items_pool=self.items_pool)

        self.assertCountEqual(shop.items, [self.item_1, self.item_2, self.item_3, self.item_4, self.item_5,
                                           self.item_6, self.item_7, self.item_8, self.item_9, self.item_10,
                                           self.item_11, self.item_12, self.item_13, self.item_14, self.item_15])
