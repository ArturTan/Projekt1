#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from customized_hack_power import hack_calculator

class TestHackCalculator(TestCase):
    pass

    def test_customization(self):
        hack="advantage"
        letters={'a': 1, 'd': 2, 'e': 5,
                 'g': 2, 'n': 1, 't': 4, 'v': 7}
        phrases={"ad": 10, "ant": 13, "age": 24,
                 "van": 13, "tag": 5}
        self.assertEqual(hack_calculator(hack, letters, phrases), 74)

        
def create_test(hack, power):
    def check_test(self):
        self.assertEqual(hack_calculator(hack), power)
    return check_test

hacks = ["baaca", "babacaba", "aabacabaaaca", "abc", "baad"]
powers = [31, 55, 81, 6, 0]
      
for num, hack, power in zip(list(range(len(hacks))), hacks, powers):
    test_method = create_test(hack, power)
    test_method.__name__ = 'test_fn_{}'.format(num)
    setattr(TestHackCalculator, test_method.__name__, test_method)
    
   
        
        
