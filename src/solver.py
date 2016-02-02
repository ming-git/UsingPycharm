# !/usr/bin/env python3
# coding=utf-8
"""Learn to use PyCharm"""

import math

# <editor-fold desc="Description">
_author_ = 'ZHU Quanming'
_email_ = 'zhuquanming@me.com'
_project_ = 'UsingPyCharm'


class Solver(object):
    """
    first class
    """

    @staticmethod
    def demo(a, b, c) -> tuple:
        """二元一次方程求解"""

        d = b ** 2 - 4 * a * c
        if d >= 0:
            discriminant = math.sqrt(d)
            root1 = (-b + discriminant) / (2 * a)
            root2 = (-b - discriminant) / (2 * a)

            print(root1, root2)

            return root1, root2
        else:
            raise Exception
# </editor-fold>


Solver().demo(2, 3, 1)
