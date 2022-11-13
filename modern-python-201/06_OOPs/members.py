"""
Class can have class variables as well as instance variables.

Class variables are shared across all instances while instance
variable are only limited to that particular instance.
"""


class Box:

    # class variable/member
    box_type = "Packaging Carton"
    color = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self) -> str:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


box_1 = Box(23, 45)

print(box_1)
print(box_1.box_type)
print(box_1.color)
