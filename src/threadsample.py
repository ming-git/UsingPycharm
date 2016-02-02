# coding=utf-8

"""
Using PyCharm Example, Use to test the run/debug function

"""

import threading
import time


def get_thread_name():
    """
    Sample
    :return:
    """
    thread_current = threading.current_thread()
    return thread_current.name


def print_time(delay):
    """Define a function for the thread.
    :param delay:
    """

    thread_name = get_thread_name()
    count = 0

    while count < 8:
        time.sleep(delay)
        count += 1

        print("{}:{}".format(thread_name, time.ctime(time.time())))

# Create two threads as follows

t1 = threading.Thread(target=print_time, args=(1,))
t2 = threading.Thread(target=print_time, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

