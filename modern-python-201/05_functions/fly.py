"""
Since Zortan has less gravity, residents can fly if they weight
less than or equal to 15 kgs in Zortan weight.

Louis wants to see which of his friends can fly.

Info:
-----
Our functions do only one thing at a time, this is called as `Single
Responsibility Principle` and important aspect of programming.
"""
from typing import Final
from weight import calc_weight

MAX_FLYING_WEIGHT: Final[float] = 15


def can_fly(weight: float) -> bool:
    return weight <= MAX_FLYING_WEIGHT


def flying_friend(friends):
    for name, earth_weight in friends.items():
        zortan_weight = calc_weight(earth_weight)
        if can_fly(zortan_weight):
            print(f"{name}: {zortan_weight} kgs can fly on Zortan!")
        else:
            print(f"{name}: {zortan_weight} kgs can NOT fly on Zortan!")


def main() -> None:
    friends: dict[str, float] = {
        "Cece": 54,
        "ROKO": 88,
        "Chiko": 50,
        "Niko": 102,
        "Ziko": 90,
    }
    flying_friend(friends)


main()
