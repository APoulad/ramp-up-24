import unittest
from String_to_int_very_easy import string_int
from addition_very_easy import addition
from discount_easy import dis
from Stuttering_Function_easy import stutter

class challenges_testing(unittest.TestCase):

    def test_num(self):
        self.assertEqual(4, string_int("4"))

    def test_zero(self):
        self.assertEqual(0, string_int("0"))

    def test_add(self):
        self.assertEqual(5, addition(2, 3))

    def test_discount(self):
        self.assertEqual(75, dis(100, 25))

    def test_stutter(self):
        self.assertEqual("an... an... anamongolia?", stutter('anamongolia'))