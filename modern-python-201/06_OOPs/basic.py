"""
Class:
------
`Class` are just like a building blueprint, they provide you with the
specifications of how to construct a building. It is upto you when and
how you build the building.

Instance:
---------
When you actually construct a building out of the blueprint, it is called as
an `Instance` or `Object` of the class. So, both are related but essential
different terminology.

Class = Blueprint, Instance = Building

Methods:
--------
These are just normal functions, but defined to alter the behavior of your instance or class.
Since they are tied to a class, they are called as methods. Their behavior is dependent on
the structure you define in the class.

When to use Class:
------------------
Use classes only when you need `Structure` and `Behavior` together.

If you only need structure, then choose from any existing data structures such as
list, tuple, dictionary, queue, etc. Just need a behavior? Then just create a function
that transforms your data.

"""
# ------------------------------------------------------------------------------------
class SomeClass:
    """Defines an empty class"""

    pass


# print(SomeClass)

# ------------------------------------------------------------------------------------


class Person:
    """Define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """Official representation of class"""
        return "<class 'Person'>"

    def __str__(self) -> str:
        """This magic method provides string representation of an instance"""
        return f"Person: {self.first_name} {self.last_name}"

    def greeting(self) -> None:
        """Method that prints greeting message"""
        print(f"{self.first_name} says hello 👋🏿")


# Creating an `instance ` of class/type `Person`
p1 = Person("Samuel", "Kiroko")
p2 = Person("Joyce", "Kiroko")
print(p1)
print(p2)

# Both are different instance of the same class at different memory location
print(f"P1 is located at memory address: {hex(id(p1))}")
print(f"P2 is located at memory address: {hex(id(p2))}")

# Calling methods on particuler instances
p1.greeting()
p2.greeting()
