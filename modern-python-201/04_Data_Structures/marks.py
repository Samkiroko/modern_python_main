"""

Dictionary:
-----------

Louis has given his exams and received marks. Let's check
out how did he fare.

Dictionary makes it easy to have key-value pairs.

Info:
-----
Lookups are very fast!!!
"""
# ---------------------------------------------------------------------------
# Creating dictionary
# ---------------------------------------------------------------------------

marks: dict[str, int] = {
    "Maths": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "pysics": 63,
}

print(f"Marks: {marks}")

# ---------------------------------------------------------------------------
# Louis wants to check out all the subjects (keys)
# ---------------------------------------------------------------------------

for subject in marks.keys():
    print(subject)

# ---------------------------------------------------------------------------
# Louis want to check out all the marks (Values)
# ---------------------------------------------------------------------------

for score in marks.values():
    print(score)

# ---------------------------------------------------------------------------
# Louis wants to check out all the suject & marks together (key-Value)
# ---------------------------------------------------------------------------

for subject, score in marks.items():
    print(f"{subject}: {score}/100")

# ---------------------------------------------------------------------------
# Louis want to check if he passed all of the subjects, Passing mark 50
# ---------------------------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASSED")
    else:
        print(f"{subject}: FAILEd!!!!")

# ---------------------------------------------------------------------------
# Louis request revaluation of his  English paper, there was a totalling
# mistake and right mark are 70
# ---------------------------------------------------------------------------

marks["English"] = 70

print(f"Louis scored {marks['English']} in English")

# ---------------------------------------------------------------------------
# Louis want to add geography
# ---------------------------------------------------------------------------

marks["Geography"] = 78

# ---------------------------------------------------------------------------
# Louis want to check if he has pass
# ---------------------------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASSED")
    else:
        print(f"{subject}: FAILEd!!!!")


# ---------------------------------------------------------------------------
# Friends at Zortan wants's to know how much Louis scored in python
# ---------------------------------------------------------------------------

# Alternative 1
# -------------

python_score = marks["Python"]
print(f"Louis score {python_score} in python")

# Alternative 2 preferred option
# -------------

python_score = marks["Python"]
print(f"Louis score {python_score} in python version 2")

# ---------------------------------------------------------------------------
# Why using get()
# `get()` doe not throw an error in case the item is not available
# ---------------------------------------------------------------------------

java_score = marks.get("Java")

if java_score is None:
    print("Louis did not take Java")
else:
    print(f"Louis score {java_score} in Java")

# ---------------------------------------------------------------------------
# Louis want to delict English form marks dict
# ---------------------------------------------------------------------------

del marks["English"]

print(marks)
