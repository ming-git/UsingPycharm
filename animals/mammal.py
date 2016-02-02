# coding=utf-8

"""
test class declaration

"""
from animals.carnivore import Carnivore
from animals.herbivore import Herbivore


class Mammalia(object):
    extremities = 4

    def feeds(self):
        print("milk")

    def proliferates(self):
        pass


class Marsupial(Mammalia):
    def proliferates(self):
        print("poach")


class Eutherian(Mammalia):
    def proliferates(self):
        print("placenta")


class TasmanianDevil(Marsupial, Carnivore):
    pass


class Duckbill(Marsupial, Herbivore):
    pass


class Cat(Carnivore, Eutherian):
    pass


class Tiger(Eutherian, Carnivore):
    pass


class Cow(Eutherian, Herbivore):
    pass


Cat().feeds()
