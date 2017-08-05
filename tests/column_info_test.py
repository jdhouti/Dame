import sys
sys.path.append('../src')

import column_info as ci
import unittest

class TestColumnInfo(unittest.TestCase):
    def setUp(self):
        self.obj = ci.Column_Info('Iris.csv', 'Species')

    def test_get_type(self):
        print(self.obj.get_type())

if __name__ == '__main__':
    unittest.main()
