state_capitals = {"Washington":"Olympia", "Oregon":"Salem", "California":"Sacramento"}
print(len(state_capitals))
#print(state_capitals["Washington"]) #Like with list and string, use bracket notations to access the values

state_capitals["Washington"] = "Aberdeen" #Dictionary are mutuable data types. Meaning we can add, modify or remove key values.
state_capitals["Texas"] = "Austin" #To add a new key:value element to the print statement.
print(state_capitals)
del state_capitals["California"] #To delete key:value items
print(state_capitals) 
state_capitals.pop("Oregon") #Also use the pop feature to delete items.
print(state_capitals)