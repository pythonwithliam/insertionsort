import unittest
import insertion_sort as ins

class TestSuite(unittest.TestCase):
    test_arr = [4, 2, 6, 3, 7, 8, 1, 9, 5]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_iterative_insertion_sort(self):
        self.assertEqual(self.sorted_arr,
                         ins.iterative_insertion_sort(self.test_arr))

    def test_recursive_insertion_sort(self):
        self.assertEqual(self.sorted_arr,
                         ins.recursive_insertion_sort(self.test_arr,
                                                      len(self.test_arr)))

    def test_binary_insertion_sort(self):
        self.assertEqual(self.sorted_arr,
                         ins.binary_insertion_sort(self.test_arr))
