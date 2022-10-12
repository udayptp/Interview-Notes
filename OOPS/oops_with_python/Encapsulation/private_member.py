"""Private Member
We can protect variables in the class by marking them private. To define a private variable add two underscores as a prefix at the start of a variable name.

Private members are accessible only within the class, and we can’t access them directly from the class objects.

Example:
"""


class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)
emp.show()

# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)

# accessing private data members raise attribute error
print('Salary:', emp.__salary)

"""
In the above example, the salary is a private variable. As you know, we can’t access the private variable from the
outside of that class.
We can access private members from outside of a class using the following two approaches

Create public method to access private members
Use name mangling 

Name mangling---
We can directly access private and protected variables from outside of a class through name mangling. 
The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, 
like this _classname__dataMember, where classname is the current class, and data member is the private variable name.

"""

# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
