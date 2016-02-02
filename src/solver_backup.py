"""
Learn to use PyCharm

Pycharm Tutorial learning
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

_author_ = 'ZHU Quanming'
_email_ = 'zhuquanming@me.com'
_project_ = 'UsingPyCharm'


class Solver:
    """
    Demo to show how to use PyCharm
    """

    @staticmethod
    def calculate():
        """
        Show the x**2 -2
        :rtype: None, Print the result directly on screen
        """
        a = int(input('a '))
        b = int(input('b '))
        c = int(input('c '))

        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)

            print(root1, root2)
        else:
            print('error')


Solver().calculate()
