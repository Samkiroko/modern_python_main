"""
Variable & Keyword Arguments:
-----------------------------

What happens if we don't know before hand how many arguments we are
going to receive? We can handle this situation by using variable &
keyword arguments syntax.

Info:
-----
We will first look at unpacking first.
"""
# -------------------------- Unpacking --------------------------------

from typing import Any
from unicodedata import category


fname, sname = "samuel", "kiroko"

print(fname)
print(sname)

# -------------------------- Unpacking list --------------------------------

first, *rest = ["Cece", "Roko", "Chiko", "Niko"]

print(first)
print(rest)

# -------------------------- Variable Argument --------------------------------
def unknown_friends(*args: str) -> None:
    for friend in args:
        print(friend)


unknown_friends("Cece", "Roko", "Chiko", "Niko", "Jake", "Mario")


# -------------------------- Variable Argument: Dictionary --------------------------------


def unknown_product(**kwargs: Any):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


unknown_product(name="Pizza", price=3.99, topping="olives", extra_cheese=True)


# -------------------------- Variable Argument both --------------------------------


def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice(
    "Sneaker",
    "black",
    "white",
    brand="nike",
    category="Air Jordans",
    Price=899.99,
    in_stock=False,
)
