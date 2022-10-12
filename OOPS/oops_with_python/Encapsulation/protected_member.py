"""
Salary: 10000
Protected Member
Protected members are accessible within the class and also available to its sub-classes. To define a protected
member, prefix the member name with a single underscore _.

Protected data members are used when you implement inheritance and want to allow data members access to only
child classes.

Example: Proctecd member in inheritance.
"""

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)