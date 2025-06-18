# Use of static method in Python
"""
In Python, @staticmethod is a decorator that defines a method that does not access or modify the class or instance (i.e., no self or cls).
It's bound to the class only for organizational purposes, and you can call it without creating an instance of the class.

Key points:
- No access to self (instance) or cls (class).
- Can be called using ClassName.method() or instance.method().
- Used when the method logically belongs to the class but doesn't need class or instance data.
"""

# Example
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def multiply(a,b):
        return a * b

# Call without creating an instance
print(MathUtils.add(3,5))
print(MathUtils.multiply(4, 6))

# Also callable via an instance (but not recommended)
utils = MathUtils()
print(utils.add(10, 20))
print("\n==============================================================\n")

# -------------------------------------------------------------------------------------------------

# Use of class method in Python
"""
A class method that is bound to the class, not the instance. It takes `cls` (not self) as its first argument, where  
`cls` refers to the class itself.

✅ Key Characteristics:
- Decorated with the `@classmethod`
- Can access or modify class-level variables (but not instance level ones)
- Can be called using `ClassName.method()` or `instance.method()`


🤔 Why Do We Need It?
We use class methods when:
1. We need to modify or access class variables.
2. We want to provide alternative constructors (e.g. creating objects in different ways).
3. We want to write utility methods that are logically tied to the class, but not specific to any instance.  
"""

# Let's see the example
class Employee:

    raise_percentage = 1.05 # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary *= self.raise_percentage

    @classmethod
    def set_raise_percentage(cls, amount):
        cls.raise_precentage = amount

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, float(salary))

# Use classmethod to raise percentage
Employee.set_raise_percentage(1.10)

# Create instance using class method as an alternative constructor
emp1 = Employee.from_string("Alice-60000")
print(emp1.name, emp1.salary)

emp1.apply_raise()
print(emp1.salary)

print("\n==============================================================\n")

# ------------------------------------------------------------------------------------------------------

# Example of lambda function
square = lambda x: x**2
print(square(5)) # Output: 25
print()

# Another example of lambda function
addition = lambda x,y: x+y
print(addition(2,3)) # Output: 5
print()

# map function: Applies a function to each item in an iterable
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x,  nums))
print(squared)
print()

# filter function: Filters conditions based on a condition (return only items where the function is True)
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x%2==0, nums))
print(even)
print()

# reduce(): Used to reduce a single value. (Must be imported from functool)
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x,y: x*y, nums)
print(product)
print()