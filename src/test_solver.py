from unittest import TestCase

from solver import Solver


class TestSolver(TestCase):
    def test_demo_with_negative_disc(self):
        s = Solver
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    # def test_demo(self):
    #     self.fail()
