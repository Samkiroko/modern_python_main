"""
Higher Order Functions:
-----------------------
Please note that this is a advanced topic, so it may take a couple of attempts
to understand these concepts.

Functions under the hood are just `Objects`, they can be passed to other
functions and functions can also return functions!

This data type is called as `Callable`, one which can be called or invoked.

Note:
-----
Till now we have been sending data to our functions, but sending data every time
can be expensive, instead we can send function to data!

Don't spend too much time mastering this topic, it will come naturally as you
progress with your programming skills.
"""
# -------------------------------------------------------------------------
from typing import Callable


def hello() -> None:
    """Print  hello"""
    print("Hello")


# hello is just a regular object or class of type `function`
print(hello)
print(id(hello))
print(type(hello))

# We can assign function to variable
greet: Callable[[], None] = hello  # Just assigns the object `hello` to great variable
greet()  # We can invoke/call the function using () at the end.

# ______________________________________________________________________________________

"""let's try create a universal greeter that can greet a person in multiple
ways
"""


def zola(name: str) -> str:
    return f"Zola, {name}!"


def good_morning(name: str) -> str:
    return f"Good Morning, {name}!"


def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"


# Function accepting a function
def universal_greeter(name: str, greeter: Callable[[str], str]):
    """Can great in multiple ways"""
    msg = greeter(name)
    print(msg)


universal_greeter("Samuel", zola)
universal_greeter("Samuel", good_morning)
universal_greeter("Samuel", goodbye)

# ______________________________________________________________________________________
"""
Function returning function!!
_____________________________

"""
# Function returning a function
def add_by_5(num: int) -> Callable[[], int]:
    """Add by 5"""

    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(51)
print(sum())


# Function returning a function
def unique_adder(num1: int) -> Callable[[int], int]:
    """Adds two numbers and then subtracts by 1"""

    def adder(num2: int) -> int:
        return num1 + num2 - 1

    return adder


addr = unique_adder(5)(7)
print(addr)

# ____________________________________Lambda__________________________________________________

add: Callable[[int, int], int] = lambda x, y: x + y
subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y


def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    """Performs the math operation on the numbers"""
    return operation(num1, num2)


print(calc(4, 5, add))
print(calc(4, 5, subtract))
print(calc(4, 5, multiply))
