from sys import path
path.append("../src")
import histogram
import unittest


class HistogramTest(unittest.TestCase):
    def setUp(self):
        self.obj1 = histogram.Histogram("test Histogram")

    def test(self):
        print(self.obj1.getTitle())

if __name__ == '__main__':
    unittest.main()
