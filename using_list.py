states = ["Washington", "Oregon", "California"]

#print(states[0])

""""
print(states[-1])
print(states[-2])
print(states[-3])
"""
#To access the last item in the list, and go backwards, use negative numbers i.e -1 would be California.
#List are mutable, meaning we can modify individual list items.

states[2] = "Arizona"
#print(states)
#If we want to find how many items are in a list, use "len", short for length.
#print(len(states))
states.append("New York")
print(states)
states.pop() #This is to remove an item from the list. If argument is empty, it will automatically remove the last item on the list.