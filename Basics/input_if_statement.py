def max_num(num1, num2, num3):  # Strings can be used
    if num1 >= num2 and num1 >= num3:  # Question
        return num1  # Answer
    elif num2 >= num1 and num2 >= num3:  # 2nd Question
        return num2  # 2nd Answer
    else:
        return num3  # If not the first 2 then it has to be this


print(max_num(3, 4, 5))  # Using the def at the top so only 3 numbers used

# == > < <= >= !=
