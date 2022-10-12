"""
compile time polymorphism - method and operator overloading
compile time polymorphism feature.
Operator Overloading in Python
Python supports operator overloading. This is another type of polymorphism where an operator behaves
differently based on the type of the operands.

+ operator adds two numbers and concatenate two strings
* operator multiplies two numbers and when used with a string and int, repeats the string given int times
 and concatenate them.
"""
def add(x,y):
    return x+y
def multiply(x,y):
    return x*y

print(add(2,4))
print(add("ab","cd"))
print(multiply(2,3))
print(multiply("ab",3))