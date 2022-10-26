from random import randint

secret = randint(1, 10)

guess = int(input("Enter your guess: "))

for i in range(5):
    if guess == secret:
        print("You got it!")
    break
print("Secret", secret)


"""
a) purpose of the of break 
=> get out of the loop after input
b) keywords:
1. range
2.int
3.input
4.print
c) assignment statement
1)secret = randint(1, 10)
2) guess = int(input("Enter your guess: "))
"""

# Question 3 version 1

score_1 = int(input("score between 0 and 10 >> "))
score_2 = int(input("score between 0 and 10 >> "))
score_3 = int(input("score between 0 and 10 >> "))

score_list = [score_1, score_2, score_3]
total_sum = 0

for i in score_list:
    total_sum += i
    average = total_sum / len(score_list)
    print(f"Total sum is: {total_sum}")
    print(f"Avarage is: {average}")


# version 2

score_1 = int(input("score between 0 and 10 >> "))
score_2 = int(input("score between 0 and 10 >> "))
score_3 = int(input("score between 0 and 10 >> "))

score_list = [score_1, score_2, score_3]
total_sum = 0

for i in score_list:
    total_sum += i
    average = total_sum / len(score_list)

if average >= 8:
    print(f"Avarage is: {average}")
    print("Good work")
else:
    print(f"Avarage is: {average}")
    print("Try harder next time")
