"""
In this example, we create an Employee class by defining employee attributes such as name and salary as an
instance variable and implementing behavior using work() and show() instance methods.
"""

class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.department = dept

    def work(self):
        print("employee ", self.name, "works in department ", self.department)

    def show(self):
        print(self.name, " ", self.salary, " ", self.department)


emp = Employee("uday", 20000, "IT")
emp.work()
emp.show()

"""
** Access Modifiers in Python **

Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But
In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using
single underscore and double underscores.

Access modifiers limit access to the variables and methods of a class. Python provides three types of access
modifiers private, public, and protected.

Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class
Protected Member: Accessible within the class and its sub-classes

"""
