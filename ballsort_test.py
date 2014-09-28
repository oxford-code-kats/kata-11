import unittest
import timeit
from ballsort import Rack

class BallTests(unittest.TestCase):

    def test_empty_rack_returns_empty_list(self):
        rack = Rack()
        self.assertEqual(rack.balls, [])

    def test_add_one_ball_to_rack(self):
        rack = Rack()
        rack.add(20)
        self.assertEqual(rack.balls, [20])

    def test_add_fifteen_balls_in_wrong_order(self):
        rack = Rack()
        lottery_balls = [11,13,24,25,34,33,16,17,56,55,44,46,41,8,4]
        for ball in lottery_balls:
            rack.add(ball)
        sorted_balls = sorted(lottery_balls)
        self.assertEqual(rack.balls, sorted_balls)

    def test_sort_speed(self):
        """The time taken to add and simultaneously sort 
        15 balls on my machine (2.5Ghz, i5) with naive 
        bubblesort was 0.00630745"""
        add_speed = timeit.timeit(
                "tests.test_add_fifteen_balls_in_wrong_order();", 
                "from __main__ import BallTests; tests = BallTests()",
                number=100)
        print(add_speed) #
        self.assertTrue(add_speed < 0.01)


if __name__ == "__main__":
    unittest.main()