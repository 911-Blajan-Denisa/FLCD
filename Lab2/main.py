from LexicInserter import LexicInserter
from HashTable import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(4)

    def test_contains(self):
        obj = "a"
        obj2 = "b"
        self.ht.insert(obj)
        self.assertEqual(self.ht.contains(obj), True)
        self.assertEqual(self.ht.contains(obj2), False)
        self.ht.insert(obj2)
        self.assertEqual(self.ht.contains(obj2), True)
        self.ht.remove(obj2)
        self.assertEqual(self.ht.contains(obj2), False)


if __name__ == '__main__':
    sc = LexicInserter()
    print("Separators:", sc.separators)
    print("Operators:", sc.operators)
    print("Reserved words:", sc.reserved_words)
    print("\n")

    symbol_table = HashTable(4)
    symbol_table.insert("n")
    symbol_table.insert("x")
    symbol_table.insert("i")
    symbol_table.insert("p")

    print(symbol_table.__str__())
