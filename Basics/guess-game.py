secret_word = "danny"  # The correct answer
guess = ""  # The current guess (is changed in code)
guess_count = 0  # The start value of guesses (is changed in code)
guess_limit = 3  # The limit of guesses allowed
out_of_guesses = False  # False means can still play - code changes to stop the game

while guess != secret_word and not(out_of_guesses):
    # Starts a loop to check for guess of word and not out of guesses
    if guess_count < guess_limit  # Has the guess limit been reached
    guess = input("Guess a word: ")
    # User puts in a guess and is stored as guess
    guess_count += 1  # Adds 1 to the guess count
    else:
        # If the Guess limit has been reached (if check) change to True
        out_of_guesses = True
if out_of_guesses:  # When the loop finishes for either word right or guess count met
    print("Out of Guesses")  # Print if out of guesses is True
else:
    print("You Win!")  # Print if out of guesses is False
