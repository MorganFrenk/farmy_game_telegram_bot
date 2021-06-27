import unittest
from objects import items


class TestItems(unittest.TestCase):

    def setUp(self) -> None:
        self.item_1 = items.Item('item one', 1, 100)
        self.item_2 = items.Item('item two', 2, 200)
        self.items_1 = items.Items()

    def test_items(self):
        self.items_1.add_item(self.item_1)
        self.assertTrue(self.item_1 in self.items_1.items)


if __name__ == '__main__':
    unittest.main()
