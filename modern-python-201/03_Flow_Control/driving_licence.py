"""
Louis wants to drive a car 🚙 and wants to know if he can
apply for a driving license or not.
"""

age: int = 13

# ----------------------------------------------------
# If / Else Statement
# ----------------------------------------------------

if age < 16:
    print("You are NOT eligible for a license")
else:
    print("You are eligible for license")


# ----------------------------------------------------
# After a couple of years
# ----------------------------------------------------

age: int = 100


# if age < 16:
#     print("You are NOT eligible for a license")
# else:
#     print("You are eligible for license")


# ----------------------------------------------------
# Alternative Implementation - Without `Else` Block
# ----------------------------------------------------

# if age < 16:
#     print("You are NOT eligible for a license")

# print("You are eligible for license")


# ----------------------------------------------------
# Alternative Implementation - With elif
# ----------------------------------------------------


if age < 16:
    print("You are NOT eligible for a license")
elif(age >= 100):
  print("Too old to drive")
else:
    print("You are eligible for license")