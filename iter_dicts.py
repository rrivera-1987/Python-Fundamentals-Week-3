state_capitals = {"Washington":"Olympia", "Oregon":"Salem", "California":"Sacramento"}
#To iterate all the keys, use the for in loop
"""for state in state_capitals:
    print(state)"""

#To call out or iterate the values
"""for city in state_capitals.values():
    print(city)"""

#To iterate both keys and values
"""for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)"""
    
for state, city in state_capitals.items(): #We can speficy in the for loop header we want the current key and value using item
    print(city, "is the capital of", state)
