"""
Louis wants to drive a car 🚙 and he hears that in planet
Zortan 🪐 there is no age limit for getting a license.

`AND` Table
------------
True and True => True
False and False => False
True and False => False
False and True => False

`OR` Table
----------
True or True => True
False or False => False
True or False => True
False or True => True
"""

age: int = 13
planet: str = "Earth"

# ----------------------------------------------------
# And / Or Statement
# ----------------------------------------------------

if age < 16 and planet == 'Earth':
  print("You are NOT eligible for license on Earth 🌎")
elif age > 16 and planet == "Earth":
  print("You can apply for a license on Earth 🌎")
elif age < 16 and planet == "Zortan":
  print("You can apply for Zortanian license")
  
  
# ----------------------------------------------------
# Louis Migrate to zortan
# ----------------------------------------------------

age: int = 13
planet: str = "Zortan"



if age < 16 and planet == 'Earth':
  print("You are NOT eligible for license on Earth 🌎")
elif age > 16 and planet == "Earth":
  print("You can apply for a license on Earth 🌎")
elif age < 16 and planet == "Zortan":
  print("You can apply for Zortanian license")