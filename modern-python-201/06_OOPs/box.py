from __future__ import annotations


class Box:
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self) -> int:
        return self.side_a * self.side_b

    def __repr__(self) -> str:
        return "<class 'Box'>"

    def __str__(self) -> str:
        return f"Box => Side A: {self.side_a}, Side B: {self.side_b} "

    def __contains__(self, num: object) -> bool:
        """Use `in` operator"""
        if not isinstance(num, int):
            raise NotImplementedError
        return num in [self.side_a, self.side_b]

    def __eq__(self, __o: object) -> bool:
        """Check if two Boxes are equal"""
        if not isinstance(__o, Box):
            raise NotImplementedError
        return self.side_a == __o.side_a and self.side_b == __o.side_b

    def __le__(self, __o: object) -> bool:
        """Check if the other box is smaller"""
        if not isinstance(__o, Box):
            raise NotImplementedError
        return self.area <= __o.area


b1 = Box(3, 8)
b2 = Box(4, 4)

print(b1)
print(b2)
print("______equal________\n")
print(b1 <= b2)

print("______equal_end________")

print(4 in b1)
print(6 in b1)
