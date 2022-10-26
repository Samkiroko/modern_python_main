"""
Functions:
----------

It's all about data transformation, ideally it should:
`take something -> give something`

Or else, it causes a `side effect`.

Remember people in Zortan greet each other by saying Zola,
Louis wants to write a program which can greet any Zortan!
"""
# Invoke the `main` function


def greeter(name: str):
    """Return a greeting message"""
    return f"Zola {name}"


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    for friend in friends:
        if "Chiko" in greeter(friend):
            print(f"{friend} is cute")
        else:
            print(greeter(friend))


main()
