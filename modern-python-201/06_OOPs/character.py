class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        return "<class 'Character'>"

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Attack Power: {self.attack_power}, life: {self.life}"
        )


villain_1 = Character("Thanos", 400, 1500)
# Using key value pairs
villain_2 = Character(name="Redskull", attack_power=300, life=800)

print(villain_1)
print(villain_2)
