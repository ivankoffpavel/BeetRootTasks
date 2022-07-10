# Task 1
# Pick your solution to one of the exercises in this module.Design tests for this solution and write tests using unittest library.
import unittest
from Getindex import *
lst = ['mama','papa','Mike','Kate','Sara','Masha','Ann','Nikoletta']
it1 = iter(lst)
class GetIndexTest(unittest.TestCase):
    def test_index(self):
        self.assertEqual(get_by_index(it1,1),'papa')



if __name__ == '__main__':
    unittest.main()