import unittest
from ageiden import age

class testageiden(unittest.TestCase):
    def testage(self):
        self.assertEqual(age(29), "You're too old!")
        self.assertEqual(age(13), "You're younger!")
        self.assertEqual(age(25), "You're the same age as me!")