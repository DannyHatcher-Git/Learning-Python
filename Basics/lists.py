# Can have all 3 types of entries (number, string, boolean)
friends = ["Jon", "Danny", "Sara", "Sara", "Tia"]
print("1", friends)  # Display the list (frineds)
print("2", friends[0])  # First thing in the list
print("3", friends[-1])  # Negative number works backwards in the list
print("4", friends[1:])  # Search for everything 1 and after
print("5", friends[1:3])  # Search up to but not including
friends[1] = "Dan"  # Change the name from hear onwards in the code
print("6", friends)  # Display the new list
friends.append("Bas")  # Adding something to the end of the list
print("7", friends)
friends.insert(1, "Kelly")  # Adding something with the postition specified
print("8", friends)
friends.remove("Kelly")  # Removes this from the list
print("9", friends)
friends.pop()  # Removes an element of the list
print("10", friends)
print("11", friends.index("Jon"))  # Prints the location of "Jon"
print("12", friends.count("Sara"))  # Count the number of "Sara"
friends.sort()  # Sort in alphabetical
print("13", friends)
lucky_numbers = [4, 8, 15, 15, 23, 42]
lucky_numbers.sort()  # Ascending order
print("14", lucky_numbers)
lucky_numbers.reverse()  # Decending order
print("15", lucky_numbers)
friends.extend(lucky_numbers)  # Combines the two lists
print("16", friends)  # Printing new extended list
friends2 = friends.copy()  # Copy friends list
print("17", friends2)
friends.clear()  # Clears the list
print("18", friends)
