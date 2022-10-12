"""
Single Inheritance - When a child class inherits from only one parent class, it is called single inheritance.

Create a class named Person, with firstname and lastname properties, and a printname method:
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

"""
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
"""
class Student(Person):
  def __init__(self, fname, lname, yog):
    Person.__init__(self, fname, lname)
    self.graduationyear = yog

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

"""
Python also has a super() function that will make the child class inherit all the methods and properties from 
its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the
methods and properties from its parent.
"""

x = Student("Mike", "Olsen", 2019)

"""
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the 
parent method will be overridden.
"""