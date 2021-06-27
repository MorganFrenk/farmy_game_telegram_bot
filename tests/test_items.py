import unittest
from objects.items import Items, Item


class TestItems(unittest.TestCase):

    def setUp(self) -> None:
        self.item_1 = Item('item one', 1, 100)
        self.item_2 = Item('item two', 2, 200)
        self.items_pool = Items()
        self.items_pool.add_item(self.item_1)


    def test_add_items(self) -> None:
        self.assertTrue(self.item_1 in self.items_pool.items)

    def test_remove_items(self) -> None:
        self.items_pool.remove_item(self.item_1)
        self.assertFalse(self.item_1 in self.items_pool.items)

    def test_find_items(self) -> None:
        self.assertEqual(self.item_1, self.items_pool.find_item(self.item_1.name))

    def test_list_items(self) -> None:
        self.items_pool.add_item(self.item_2)
        self.assertEqual([self.item_1], self.items_pool.list_items_with_power(self.item_1.power))
        self.assertEqual([self.item_1, self.item_2], self.items_pool.list_items_with_power(self.item_2.power))
