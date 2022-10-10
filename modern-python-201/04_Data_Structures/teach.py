"""

Set:
----
Louis has graduated from school and now wants to teach Zortans
how to talk in English. But English is complicated, so lets try
to simplify it using Sets.

Set is all about being `unique`, it's very useful for certain operations.

Info:
-----
In a Set all values are unique
"""

# -----------------------------------------------------------------------------
# Louis wants to impress by showing some English magic, but Zortans are
# confused, they want him to first shows unique alphabets in his magic.
# -----------------------------------------------------------------------------

magic_word = "abracadabra"
unique_alphabets: set = set(magic_word)
print(f"Unique Alphabets: {unique_alphabets}")

sentence = "the big blue sky and the big blue ocean"
unique_alphabets = set(sentence)
print(f"Unique Alphabets: {unique_alphabets}")

# -----------------------------------------------------------------------------
# What happens if we want to see list of unique words instead of alphabets
# -----------------------------------------------------------------------------

word_list = sentence.split()
print(f"Word List: {word_list}")

# -----------------------------------------------------------------------------
# Extract the unique words
# Set uses carry blase and contains only values
# -----------------------------------------------------------------------------
unique_word = set(word_list)
print(f"Unique Words: {unique_word}")

# -----------------------------------------------------------------------------
# Zortans are impressed and they want to add more words to the set
# Updating a set make sure the items are unique
# Update with a iterable data type e.g list
# -----------------------------------------------------------------------------

unique_word.update(["Boy", "Green"])
print(f"Unique words: {unique_word}")

# -----------------------------------------------------------------------------
# Zortans don't like the word Green and wants to remove it
# -----------------------------------------------------------------------------

unique_word.remove("Green")
print(f"Unique Words: {unique_word}")
