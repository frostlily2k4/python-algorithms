import unittest

from algorithms.searching.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        data = [2, 5, 8, 12, 16, 23, 38]
        self.assertEqual(binary_search(data, 23), 5)

    def test_not_found(self):
        data = [2, 5, 8, 12, 16]
        self.assertEqual(binary_search(data, 20), -1)

    def test_first_element(self):
        data = [2, 5, 8, 12]
        self.assertEqual(binary_search(data, 2), 0)

    def test_last_element(self):
        data = [2, 5, 8, 12]
        self.assertEqual(binary_search(data, 12), 3)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 10), -1)


if __name__ == "__main__":
    unittest.main()