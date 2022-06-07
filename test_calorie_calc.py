
import unittest

from calorie_calc import calculate_activity

class TestCalorieCalc(unittest.TestCase):

    def test_calculate_activity_none(self):
        activity_level = 'none'
        if activity_level == 'none':
            self.assertEqual(calculate_activity(1), 1.2)


