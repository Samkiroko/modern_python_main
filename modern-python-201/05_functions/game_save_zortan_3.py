"""
Save Zortan:
------------

Let's convert the game logic into small functions.

Principles:
-----------

1. DRY - Don't Repeat Yourself -
================================
Try to keep your code as DRY as possible, group common functionality into
individual functions.

2. SRP - Single Responsibility Principle -
==========================================
Ideally one function should be responsible for only one operation.

Note:
-----
We will also learn about global & local scope of variables (Using scratch pad)
"""
# we need this for generating random nos.
from random import randint
from typing import Final

Character = dict[str, str | int]

# ________________________________life____________________________________________
# Helper Variable
hero_life = 0
villain_life = 0


def inc_hero_life(life: int) -> None:
    """Decrease Hero Life"""
    global hero_life
    hero_life += life


def dec_hero_life(life: int) -> None:
    """Increase Hero Life"""
    global hero_life
    hero_life -= life


def inc_villain_life(life: int) -> None:
    """Decrease villain Life"""
    global villain_life
    villain_life += life


def dec_villain_life(life: int) -> None:
    """Increase villain Life"""
    global villain_life
    villain_life -= life


def get_all_superheros() -> list[Character]:
    # Super Heroes
    IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
    BLACKWIDOW: Character = {
        "name": "Blackwidow",
        "attack_power": 180,
        "life": 800,
    }
    SPIDERMAN: Character = {
        "name": "Spiderman",
        "attack_power": 190,
        "life": 700,
    }
    HULK: Character = {"name": "Hulk", "attack_power": 300, "life": 1100}
    superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheros


def get_superhero(index: int) -> Character | None:
    """Returns superhero from the given index."""
    superheros = get_all_superheros()
    if index < len(superheros):
        return superheros[index]
    else:
        return None


def get_all_villains() -> list[Character]:
    # Super Villains
    THANOS: Final[Character] = {"name": "Thanos", "attack_power": 400, "life": 1500}
    REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

    # All Super Heros & Super Villains
    villains: list[Character] = [THANOS, REDSKULL, PROXIMA]
    return villains


def get_villain(index: int) -> Character | None:
    """Returns villain from the given index."""
    villains = get_all_villains()
    if index < len(villains):
        return villains[index]
    else:
        return None


def attack() -> None:

    # Attack
    for attack_num in range(3):
        # each iteration get a new hero & villain
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)
        # helper varible
        superhero = get_superhero(hero_index)
        villain = get_villain(villain_index)

        if superhero and villain:
            simulate_attack(attack_num, villain, superhero)
        else:
            print("Error! No superhero or villains to fight")


def simulate_attack(attack_num, villain, superhero):
    """Simulate the actual attack"""
    # set  life
    inc_hero_life(superhero["life"])
    inc_villain_life(villain["life"])
    print(
        f"Attack: {attack_num + 1} => {superhero['name']} is going to fight with {villain['name']}"
    )
    # Attack
    dec_villain_life(villain["attack_power"])
    dec_hero_life(superhero["attack_power"])


def win_or_loose() -> None:
    """Determine if Avenger won or lost"""
    # declare helper messages
    WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

    # print a nice separating line
    print("=" * 70)

    # win or loose
    if hero_life >= villain_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)


# _________________________________main_____________________________________________________


def main() -> None:
    """Starts the Game"""
    attack()
    win_or_loose()


# _________________________________Start Game_____________________________________________________

main()
