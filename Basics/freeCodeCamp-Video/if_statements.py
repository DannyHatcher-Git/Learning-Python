is_male = True  # Input information being used
is_tall = True  # Input information being used

if is_male:  # Question
    print("You are a male")  # Answer
else:
    print("You are not a male")  # Second Answer

if is_male or is_tall:  # or can be swapped for and
    print("You are a male or tall")
else:
    print("Your are not a male or tall")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):  # Else if
    print("You are a male that is no tall")
else:
    print("You are not male or tall")
