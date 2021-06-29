import unittest
from objects.items import Items, Item, Shop


class TestItems(unittest.TestCase):

    def setUp(self) -> None:
        self.item_1 = Item('item one', 1, 100)
        self.item_2 = Item('item two', 2, 200)
        self.items_pool = Items()

    def test_add_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertTrue(self.item_1 in self.items_pool.items)

    def test_remove_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.items_pool.remove_item(self.item_1)
        self.assertFalse(self.item_1 in self.items_pool.items)

    def test_add_multiple_items(self) -> None:
        self.items_pool.add_item([self.item_1, self.item_2])
        self.assertTrue(self.item_1 and self.item_2 in self.items_pool.items)

    def test_find_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertEqual(self.item_1, self.items_pool.find_item(self.item_1.name))

    def test_list_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.items_pool.add_item(self.item_2)
        self.assertEqual([self.item_1], self.items_pool.list_items_with_power(self.item_1.power))

        self.assertEqual([self.item_1, self.item_2], self.items_pool.list_items_with_power(self.item_2.power))

        self.assertEqual([self.item_1, self.item_2],
                         self.items_pool.list_items_with_power(10, power_limit=self.item_1.power))
        self.assertEqual([self.item_2],
                         self.items_pool.list_items_with_power(10, power_limit=self.item_2.power))

    def test_random_items(self) -> None:
        self.items_pool.add_item(self.item_1)
        self.assertTrue(self.item_1 in self.items_pool.get_random_items())

        self.items_pool.add_item(self.item_2)
        self.assertTrue(self.item_1 and self.item_2 in self.items_pool.get_random_items(amount=2))

        self.assertTrue(self.item_1 in self.items_pool.get_random_items(power=1))

        self.assertTrue(self.item_1 and self.item_2 in self.items_pool.get_random_items(power=2, amount=2))

    def test_shop_refill(self) -> None:
        shop = Shop()
        self.item_1 = Item('item', 10, 200)
        self.item_2 = Item('item', 10, 200)
        self.item_3 = Item('item', 10, 200)
        self.item_4 = Item('item', 10, 200)
        self.item_5 = Item('item', 10, 200)

        self.item_6 = Item('item', 20, 200)
        self.item_7 = Item('item', 20, 200)
        self.item_8 = Item('item', 20, 200)
        self.item_9 = Item('item', 20, 200)

        self.item_10 = Item('item', 30, 300)
        self.item_11 = Item('item', 30, 300)
        self.item_12 = Item('item', 30, 300)

        self.item_13 = Item('item', 40, 300)
        self.item_14 = Item('item', 40, 300)

        self.item_15 = Item('item', 50, 300)

        self.items_pool.add_item([self.item_1, self.item_2, self.item_3, self.item_4, self.item_5,
                                 self.item_6, self.item_7, self.item_8, self.item_9, self.item_10,
                                 self.item_11, self.item_12, self.item_13, self.item_14, self.item_15])

        shop.refill_shop(items_pool=self.items_pool)
        self.assertTrue(self.item_1 and self.item_2 and self.item_3 and self.item_4 and self.item_5 and
                        self.item_6 and self.item_7 and self.item_8 and self.item_9 and self.item_10 and
                        self.item_11 and self.item_12 and self.item_13 and self.item_14 and self.item_15 in shop.items)
