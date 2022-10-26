print("Hello world")


def check_even():
    num = int(input("Enter number>>> "))

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(num, "is odd")


check_even()
