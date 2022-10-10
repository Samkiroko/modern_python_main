"""

Tuple:
------
Time for Louis to go to school, and its time for him to
choose subjects. School doesn't want students to change
subjects after they are chosen, so they use Tuple.

Tuple is like a stricter brother of List. Once a Tuple is
created, it cannot be edited.

Info:
-----
Tuple also start from index 0
"""
# --------------------------------------------------------------------------
# Create tuple
# --------------------------------------------------------------------------

subjects: tuple[str] = ("Math", "Science", "History")
# ----------------index(  0,           1,        2  )
print(subjects)

# --------------------------------------------------------------------------
# LOuis wants to count his subjects
# --------------------------------------------------------------------------
print(f"No. of subjects: {len(subjects)}")

# --------------------------------------------------------------------------
# Louis wants to sign up for all the subjects
# --------------------------------------------------------------------------
for subject in subjects:
    print(f"Louis is signing up for: {subject}")

# ---------------------------------------------------------------------------
# Louis wants to see which is his second subject
# ---------------------------------------------------------------------------
print(subject[1])
# -------------^ Remember since tiple start from index 0, we use 1 here

# ---------------------------------------------------------------------------
# School wants Louis to take another 3 subject to get full credits
# ---------------------------------------------------------------------------

add_subjects = ("English", "Kiswahili", "Chinese")
total_subject = subjects + add_subjects
print(total_subject)

# ---------------------------------------------------------------------------
# Louis loves Python, and wants to see if it's there in his subjects
# ---------------------------------------------------------------------------

if "Python" in total_subject:
    print("Yes i love python ")
else:
    total_subject += ("python",)
    print(f"Added python on my subjects: {total_subject}")
