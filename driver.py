
# Python doesn't support abstract class by default.
# We have to use/extend the Abstract Base Class (ABC)
# In abstract class, at least there is one abstract method.
# Abstract methods are: Declaration without definaton.
# We cannot initiated objects from abstract class because it has at lease 1 method without declaration (Abstract method).

from abc import ABC, abstractmethod
import time

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass
    
    @staticmethod
    def sleep(period):
      time.sleep(period)


class Laptop(Computer):
    def process(self):
        Computer.sleep(2)
        print("It's working")


class Programer:
    def work(self, computer):
        print("Solving issues..")
        computer.process()


labObj = Laptop()

progObj = Programer()
progObj.work(labObj)


# Interfaces in Python are handled differently than in most other languages.
# Interface acts as a blueprint for designing classes.

# Abstract Vs Interface in python
# =============================== #
# Interface is a (class) file with a set of method definitions that have no code. 
# An abstract class is the same thing, but not all functions need to be empty. Some can have code

