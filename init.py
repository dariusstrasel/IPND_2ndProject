#=======================================================================================================================
# IPND Stage 2 Final Project
# Author: Darius 'Alkarion' Strasel
# Description: The following program has been designed in accordance with Udacity's Stage 2 Project requirements:
#
#=======================================================================================================================

attempts = 2 #attempts are used to track how often a user fails to answer a question.
score = 0 #asthetic variable to reward player for being adept at answering questions
activeQuestion = 0 #abstracted variable to allow all functions to refer to the same value.
questionIndex = 0 #used to iterate question ID's as a method of generating uniqueness based on ordinality.
difficulty = 1 #Used to track the difficulty selected by the player.
scoreMultiplier = 1 #Used to adjust score based on difficulty.
baseQuestionWeight = 1 #Used to define the lowest value a question is worth.
uniqueIDList = [] #list used to track used question IDs
playedQuestions = [] #list used to track questions that have already been played.
questionBank = [] #list used to store questions as structured lists
questionCount = len(questionBank) #used to track specified amount fo questions to review


def assign_unique_id():
    """Helper function which iterates upon an index to generate a new number. This is designed to be called when
    creating a question, and appending to questionBank[]."""
    global questionIndex
    global uniqueIDList
    if questionIndex not in uniqueIDList:
        uniqueIDList.append(questionIndex)
        return questionIndex
    questionIndex = questionIndex + 1
    uniqueIDList.append(questionIndex)
    return questionIndex


def create_question(questionAnswer, blankSet, questionString):
    """This function nests inputs questionAnswer, blankSet and questionString with assign_unique_id() into the
    following list structure: questionBank[ID[questionAnswer, blankSet, questionString] The ordinal positions are
    crucial for return_active_answer()."""
    qsGroup = [assign_unique_id()]
    qsGroup.append([questionAnswer, blankSet, questionString])
    questionBank.append(qsGroup)


def load_questions():
    """This functions wraps any predefined create_question() in order to execute create_question*n at once."""
    create_question(["function", "variables", "values", "lists"], ["___1___", "___2___", "___3___", "___4___"],
                    '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.''')
    create_question(["Dictionaries", "datatype", "key-value"], ["___1___", "___2___", "___3___"], '''___1___ are Python's built-in associative ___2___.
    A ___1___ is made of ___3___ pairs where each key corresponds to a value.
    Like sets, ___1___ are unordered.''')
    create_question(["comments"], ["___1___"],
                    '''Augmenting code with human readable descriptions, or ___1___, can help document design decisions.''')
    create_question(["Variable", "equality"], ["___1___", "___2___"], '''___1___s are assigned values using the = operator, which is not to be confused with the == sign used for testing ___2___.
    A ___1___ can hold almost any type of value such as lists, dictionaries, functions.''')
    create_question(["Tuple", "immutable"], ["___1___", "___2___"],
                    '''___1___s are a Python datatype that holds an ordered collection of values, which can be of any type. Python tuples are "___2___," meaning that they cannot be changed once created.''')
    create_question(["string", "changed"], ["___1___", "___2___"],
                    '''___1___s store characters and have many built-in convenience methods that let you modify their content. ___1___s are immutable, meaning they cannot be ___2___ in place.''')


def isQuestionPlayed(question):
    """This function checks if the input, question, has been played by checking if in playedQuestions[]."""
    if question in playedQuestions:
        return True
    return False


def select_question():
    """This function iterates through the questionBank[] to select a question which has not yet been played. It assigns
    this question to a global variable in order to abstract the contents of questionBank and the logic all proceding
    functions use to refer to a question."""
    global playedQuestions
    global activeQuestion
    for question in questionBank:
        if isQuestionPlayed(question) == False:
            playedQuestions.append(question)
            activeQuestion = question
            return activeQuestion


def adjust_score():
    """This function adjusts a user's score according to the difficulty modifier and prints to the terminal what their
    new score is."""
    global score
    increase = baseQuestionWeight * scoreMultiplier
    oldScore = score
    score = int(score) + increase
    print("Your score of " + str(oldScore) + " has been increased by " + str(increase) + " points, totaling to " + str(score) + "!")


def adjust_attempts():
    """This function reduces a user's attempts and checks if 0 in order to end the game."""
    global attempts
    attempts = attempts - 1
    print("You've lost one attempt!" + " You have " + str(attempts) + " remaining.")
    if attempts == 1:
        print("WARNING! You will lose the game if you answer another question incorrectly.")
    if attempts == 0:
        print("GAME OVER.")
        quit()


def player_input(word, answer):
    """This function prompts the user to fill in a blank (passed in as input 'word) and compares it to input 'answer'
    in order to determine if their answer is correct."""
    #print(answer)
    playerAnswer = None
    while playerAnswer != answer:
        playerAnswer = input("Please enter the correct answer for: " + word + " ")
        if playerAnswer == answer:
            adjust_score()
        elif playerAnswer != answer:
            adjust_attempts()
    return playerAnswer


def text_in_qs(word, blankSet):
    """This function will check the contents of 'blankSet' in comparison to 'word' and return 'word' if it finds it
    within itself. aka the 'buddha' function."""
    for tiq in blankSet:
        if tiq in word:
            return tiq
    return None


def return_active_answer(blank):
    """This nifty function will compare input 'blank' with the reciprocal index of the activeQuestion[1][0] to return
    the respective answer for the blank. """
    for index, item in enumerate(activeQuestion[1][1]):
        if blank == item:
            return activeQuestion[1][0][index]


def lower(text):
    str = input
    return str.lower()


def difficulty_selector():
    """This function prompts the user to select their difficulty and describe how difficulty affects gameplay."""
    global difficulty
    playerAnswer = str(input("Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: "))
    while playerAnswer not in ["1", "2", "3"]:
        playerAnswer = input("Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: ")
    if playerAnswer.lower() in ["easy", "normal", "hard"]:
        playerAnswer = input("Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: ")
    if playerAnswer in ["3"]:
        difficulty_init("HARD", "3", 3, 1)
    elif playerAnswer in ["2"]:
        difficulty_init("Normal", "2", 2, 2)
    elif playerAnswer in ["1"]:
        difficulty_init("EASY", "1", 1, 3)
    print()
    return playerAnswer


def difficulty_init(difficultyString, difficultyValue, scoreAdjuster, attemptCount):
    """This function allows a call to set the game difficulty without repetitious if-trees."""
    global scoreMultiplier
    global attempts
    global difficulty
    difficulty = difficultyValue
    attempts = attemptCount
    scoreMultiplier = scoreAdjuster
    print()
    print("You've selected " + difficultyString + ". This gives you "
          + str(attempts) + " attempt(s) to solve each question while gaining " + str(scoreMultiplier) + "x points.")


def attempt_and_score_text():
    """This function prints out a colored graphic to the player representing their score and attempts."""
    print("(" + "X" * attempts + ")" + " (" + "#" * score + ")")


def play_game(inputString, blankSet):
    """This function compares inputString to blankSet to determine when and where to prompt the user for an answer. It
    will also mutate inputString to return a new question with its respective blanks filled as they are answered
    correctly by the player."""
    replaced = []
    stringaslist = inputString.split()
    print("Read the following sentence(s) and fill in the blanks when prompted... ")
    attempt_and_score_text()
    print("=" * 103)
    print(inputString)
    print()
    for text in stringaslist:
       if text_in_qs(text, blankSet) != None:
           replaced.append(text.replace(text_in_qs(text, blankSet), player_input(text_in_qs(text, blankSet), return_active_answer(text_in_qs(text, blankSet)))))
           print()
           attempt_and_score_text()
           print("=" * 103)
           newList  = str(" ".join(replaced + stringaslist[len(replaced):]))
           print(newList)
           print()
       else:
           replaced.append(text)

def prompt_question_count():
    """This function allows the player to define how many question they want to review."""
    global questionCount
    playerAnswer = input("How many questions would you like to review?" + "("
                         + str(1) + "-" + str(len(questionBank)) + ") ")
    questionCount = playerAnswer


def game_controller(start=False):
    """This function serves as a wrapper to call all preceding functions. It also will not execute unless explicitly
    passed in as True."""
    load_questions()
    if start == True:
        #print("=" * 103 )
        print(" " * 28 + "Welcome to Alkarion's IPND Quiz Project!")
        #print("=" * 103 )
        prompt_question_count()
        difficulty_selector()
        while len(playedQuestions) < int(questionCount):
            select_question()
            play_game(activeQuestion[1][2], activeQuestion[1][1])
            print()
        print("Congratulations! You reviewed all the questions!")
    return None

game_controller(True)
