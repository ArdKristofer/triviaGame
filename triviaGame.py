import random
import triviaQA

# This is a simple trivia game that will prompt the user
# to roll a for random number. Based on the number the user
# rolls, they will be presented with a question. Their answer
# will be checked and return a value of correct or incorrect.

# Let the user choose between rolling for a random number or 
# exiting the game. Check whether the user entered a valid value
diceRoll = input("Please press enter to pick a random number or press 'q' to exit. ")
while diceRoll != "q" and diceRoll != "":
    diceRoll = input("Please press enter to pick a random number or press 'q' to exit. ")
if diceRoll == "q":
    exit()
elif diceRoll == "":
    randomNumber = (random.randint(1, 10))
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
    # Allow the user the ability input their answer in any case
    answer3Lower = [i.lower() for i in triviaQA.answer3]
    result3Lower = [j.lower() for j in result3Sorted]
    if result3Lower == answer3Lower:
        print("That's correct!")
    else:
        print("Sorry the correct answer is Germany, Italy, and Japan..")
elif randomNumber == 4:
    print(triviaQA.question4)
    result4 = input("Type your answer here: ")
    if result4.casefold() == triviaQA.answer4.casefold():
        print("Yes! That's correct!")
    else:
        print("Sorry the answer is an octagon...")
elif randomNumber == 5:
    print(triviaQA.question5)
    result5 = input("Type your answer here: ")
    if result5.casefold() == triviaQA.answer5.casefold():
        print("Excellent job!")
    else:
        print("Sorry...the answer is the fear of dogs..")
elif randomNumber == 6:
    print(triviaQA.question6)
    result6 = input("Type your answer here: ")
    if result6.casefold() == triviaQA.answer6.casefold():
        print("Correct!")
    else:
        print("No..the answer is Ferdinand Magellan..")
elif randomNumber == 7:
    print(triviaQA.question7)
    result7 = input("Type your answer here: ")
    if result7.casefold() == triviaQA.answer7.casefold():
        print("Yes! That's right!")
    else:
        print("Sorry the correct answer is Samsung")
elif randomNumber == 8:
    print(triviaQA.question8)
    result8 = input("Type your answer here: ")
    if result8.casefold() == triviaQA.answer8.casefold():
        print("Great answer! It's correct!")
    else:
        print("Sorry..that answer is not right. The correct answer is Pacific Ocean..")
elif randomNumber == 9:
    print(triviaQA.question9)
    result9 = input("Type your answer here: ")
    if result9.casefold() == triviaQA.answer9.casefold():
        print("Awesome! That's right!")
    else:
        print("Unfortunately the correct answer is brown..")
elif randomNumber == 10:
    print(triviaQA.question10)
    result10 = input("Type your answer here: ")
    if result10.casefold() == triviaQA.answer10.casefold():
        print("Amazing! That's correct!")
    else:
        print("No sorry..the right answer is Coca Cola..")