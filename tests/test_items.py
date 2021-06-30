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
        self.item_1 = Item('item', 19, 200)
        self.item_2 = Item('item', 39, 200)
        self.item_3 = Item('item', 79, 200)
        self.item_4 = Item('item', 159, 200)
        self.item_5 = Item('item', 319, 200)

        self.items_pool.add_item([self.item_1, self.item_2, self.item_3, self.item_4, self.item_5])

        shop.refill_shop(items_pool=self.items_pool, pool_amount=1)

        self.assertCountEqual(shop.items, [self.item_1, self.item_2, self.item_3, self.item_4, self.item_5])
