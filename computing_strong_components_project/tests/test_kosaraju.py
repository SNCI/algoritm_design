"""
       File : test_kosaraju.py
     Author : Drew Verlee
       Date : 22.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test cases for Coursera Algorithms 1 class assignment 4
"""

import unittest
from computing_strong_components_project.main.kosarajus import kosaraju
class TestKosaraju(unittest.TestCase):
    """test kosarajus Algorithm against files contained in data"""


    def test_class_example(self):
        # how to represent the graph?
        expected = "3,3,3,0,0"
        result = kosaraju('../data/test_data_from_class_kosaraju.txt')
        self.assertSequenceEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
