import sys
sys.path.append('../src')

import data_analysis as da
import unittest

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.obj1 = da.Data_Analysis("/Users/Julien/Downloads/Iris.csv")

    # def testGetSummary(self):
    #     print(self.obj1.get_summary_statistics())

    def testGetHistogram(self):
        self.obj1.get_histogram('PetalLengthCm', 'cm').show()

    # def testScatterPlot(self):
    #     self.obj1.get_scatter_plot('SepalLengthCm', 'SepalWidthCm')

    # def testGetColumns(self):
    #     print(self.obj1.get_columns())

if __name__ == '__main__':
    unittest.main()
