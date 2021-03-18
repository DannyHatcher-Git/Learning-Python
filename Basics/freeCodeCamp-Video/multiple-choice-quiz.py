# An array of questions with muliple answers seporated by lines for a nicer output (\n)
question_prompts = [
    "What color are Apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananase?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]


class Question:  # Creating a class for questions (assigning attributes)
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# An array that stores all of the questions with the correct answers
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):  # Defining a function to run
    score = 0  # For storing the score of the person
    for Question in questions:  # A loop to go through the questions array
        # The players answer is the input (the question prompt shows for reference)
        answer = input(Question.prompt)
        if answer == Question.answer:  # Asks if the answer was right
            score += 1  # If the answer was right add 1 to score
    # the output after all questions are answered.
    print("You got " + str(score)+"/"+str(len(questions))+" correct")


run_test(questions)  # Calling the function to run when the script is played.
