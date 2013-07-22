"""
       File : test_kosaraju.py
     Author : Drew Verlee
       Date : 22.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test cases for Coursera Algorithms 1 class assignment 4
"""

import unittest
from collections import defaultdict, Counter
from computing_strong_components_project import kosarajus
class TestKosaraju(unittest.TestCase):
    """test kosarajus Algorithm against files contained in data"""

    def setUp(self):
        kosarajus.s = None # leaders in 2nd pass
        kosarajus.explored = set()
        kosarajus.leaders = Counter()
        kosarajus.vertex_to_finishing_time = defaultdict(int)
        kosarajus.t = 0
        kosarajus.second_loop = False


    def test_class_example(self):
        expected = "3,3,3,0,0"
        result = kosarajus.kosaraju('../data/test_data_from_class_kosaraju.txt')
        self.assertSequenceEqual(expected, result)

    # def test_unconnected(self):
    #     """ not actual sure about this one"""
    #     expected = "1,1,0,0,0"
    #     result = kosarajus.kosaraju('../data/test_data_kosaraju_unconnected.txt')
    #     self.assertSequenceEqual(expected, result)

    def test_data_kosaraju_Stecko_case_1(self):
        expected = '3,3,1,1,0'
        result = kosarajus.kosaraju('../data/test_data_kosaraju_Stecko_case_1.txt')
        self.assertSequenceEqual(expected, result)

    def test_data_kosaraju_Stecko_case_2(self):
        expected = '7,1,0,0,0'
        result = kosarajus.kosaraju('../data/test_data_kosaraju_Stecko_case_2.txt')
        self.assertSequenceEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
