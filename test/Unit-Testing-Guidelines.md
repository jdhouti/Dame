# Unit Testing Guidelines
To make it easier for contributors to follow testing in the **test** folder, it
is recommended that all contributors follow these instructions/guidelines.  
More documentation for the **unittest module** can be found [here](https://docs.python.org/3/library/unittest.html).

## Steps to create a unit test script
1. Import the module: `import unittest`
2. Create a testing class:
   ```python
   class ClassTest(unittest.TestCase):
   ```
3. Create all of the testing functions that you may need:
   ```python
   class ClassTest(unittest.TestCase):
     def first_method_test(self):
       self.assertEqual(testing conditions here)
   ```
4. If there is setting up to do, you can use `setUp(self)` method in your class. The `setUp()` method is usually written at the top of the class and it is automatically ran before every test function in the class the method is written in.
   ```python
   class ...
      def setUp(self):
         # set up instruction go here.
   ```
5. To execute the tests, make sure to include this at the bottom of your script:
   ```python
   if __name__ == '__main__':
    unittest.main()
   ```
