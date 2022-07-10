# Task 2
# Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write
# tests using unittest library
import unittest
from Phonebookcheck import seek_adres
class TestPhonebook(unittest.TestCase):
    def Test_seek_adres(self):
        text = seek_adres('Lvivska,25')
        self.assertEqual(text,['Lvivska,25'])
if __name__ == '__main__':
    unittest.main()