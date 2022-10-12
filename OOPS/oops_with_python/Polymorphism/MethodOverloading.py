"""
Unlike many other popular object-oriented programming languages such as Java, Python doesn’t support
compile-time polymorphism or method overloading. If a class or Python script has multiple methods with
the same name, the method defined in the last will override the earlier one.

Python doesn’t use function arguments for method signature, that’s why method overloading is not supported in Python.
"""

def add(x,y):
    return x+y

def add(x,y,z):
    return x+y+z

print(add(2,3))