"""
In Python, abstraction can be achieved by using abstract classes.
An Abstract class can contain the both method normal and abstract method.
we cannot create objects for the abstract class.
Python provides the abc module to use the abstraction in the Python program.


A class that consists of one or more abstract method is called the abstract class. Abstract methods do not 
contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its 
definition in the subclass. Abstraction classes are meant to be the blueprint of the other class.
"""
from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

"""
Explanation -
In the above code, we have imported the abc module to create the abstract base class. We created the Car class that 
inherited the ABC class and defined an abstract method named mileage(). We have then inherited the base class from 
the three different subclasses and implemented the abstract method differently. We created the objects to call the 
abstract method.
"""