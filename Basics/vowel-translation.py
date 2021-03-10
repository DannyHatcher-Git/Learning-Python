def translation(phrase):
    translation = ""  # Empty string
    for letter in phrase:  # For each letter in the phrase
        if letter in "aeiouAEIOU":  # Check to see if it is included in the string
            translation = translation + "g"
            # If it is make the new phrase (translation) a g
        else:
            translation = translation + letter
            # If it is not in the string put the letter it was
    return translation


print(translation(input("Enter a phrase: ")))
# Asking user for an input and displaying the translation
