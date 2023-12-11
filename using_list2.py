states = ["Washington", "Oregon", "California"]

# If we want to iterate a fixed number of lists items, we would use the for loop.
# In this case we would use the for x in range(start, stop, step)
#print(x).
""""
for x in states:
    print(x)
"""
"""for state in states:
    state = state.lower() # This will put the initial capital letter to a lower case letter in each of the list items.
    print(state)

print("Washington" in states) #This expression will evaluate as true if there is an item that matches Washington
"""
# Concatenating lists: to combine two list togethers, using the addition operator.

states2 = ["Arizona", "Puerto Rico", "Ohio", "Virginia", "New York"]
best_states = states +  states2
print(best_states)
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])

# To slice a list, use the colon : 
# Slicing notations can be used in different ways. You can leave the first part empty and then the index number after the colon
# Ex: [:2] This will start at the beggining and stop at the second index number
# [4:] Will start at number 4 index number and go to the end