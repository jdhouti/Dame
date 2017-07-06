import sys
sys.path.append('../src')

import file_name_generator as fng
import unittest

class TestNameGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = fng.Name_Generator()

    # def testGenerate_Name(self):
    #     # run the generate_name function from the Name_Generator class
    #     a = self.generator.generate_name()
    #     b = self.generator.generate_name()
    #     print(self.generator.get_generatedNames())

    def testGetFileName(self):
        print(self.generator.get_file_name("/Users/Julien/Downloads/Iris.csv"))

if __name__ == '__main__':
    unittest.main()
