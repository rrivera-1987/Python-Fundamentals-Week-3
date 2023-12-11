# numbers_set = {1, 2, 3}
# numbers_set = {1, 2, 3, 4, [5, 6]} # Square brackets denoted lists, and lists are immutable date types. Cannot be used.
# numbers_set = {1, 2, 3, 4, (5, 6)} # tuples are denoted with parentheses and are mutable.

words_set = {"Alpla", "Bravo", "Charlie"} # strings are immutable data type.
""" abcd = ""
for word in words_set:
    abcd += word # iterating through the set by concactenating the value using addition assingment operator.
print(abcd) """

""" if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set") """

words_set.add("Delta") # Method add, to add item to the set
print(words_set)
words_set.discard("Bravo") # Method discard, to take out an item from the set
print(words_set)