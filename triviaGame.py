import random
import triviaQA

# This is a simple trivia game that will prompt the user
# to roll a for random number. Based on the number the user
# rolls, they will be presented with a question. Their answer
# will be checked and return a value of correct or incorrect.

# Prompt the user to press enter to roll for a random number
diceRoll = input("Press enter to pick a random number! ")

# Determine whether the user's input is valid
while diceRoll != (""):
    diceRoll = input("Please press enter to pick a random number or press 'q' to exit. ")
    if diceRoll == "q":
        exit()
else:
    randomNumber = (random.randint(1, 3))
    print("You chose the number " + str(randomNumber) + "!")

# Let's ask some questions
if randomNumber == 1:
    print(triviaQA.question1)
    # Accept upper and lowercase spellings
    result1 = input("Type your answer here: ")
    if result1.casefold() == triviaQA.answer1.casefold():
        print("That is correct!")
    else:
        print("Sorry the answer is " + triviaQA.answer1 + "..")
elif randomNumber == 2:
    print(triviaQA.question2)
    result2 = input("Type your answer here: ")
    if result2 == ("50") or result2.casefold() == triviaQA.answer2.casefold():
        print("That is correct!")
    else:
        print("Sorry the correct answer is " + triviaQA.answer2 + "..")
elif randomNumber == 3:
    print(triviaQA.question3)
    result3 = input("Type your answers here: ")
    # Store the user's input in a list
    result3List = result3.split()
    # Sort the list so that it corresponds to the correct answer
    result3Sorted = sorted(result3List)
    if result3Sorted == triviaQA.answer3:
        print("That's correct!")
    else:
        print("Sorry the correct answer is Germany, Italy, and Japan..")