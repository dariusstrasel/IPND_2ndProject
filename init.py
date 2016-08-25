#=======================================================================================================================
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#Todo: Remove unecessary comments
#Todo: Add docstrings for all functions
#Todo: Clean up logic around execution
#Todo: Add in difficulty modifers for attempts and score calculation
#Todo: Have score returned when game is won or lost.
#Todo: Maybe: Control how many questions are asked?
#Todo: Naybe: Modify select_question to allow parameter to select specific question
#=======================================================================================================================

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

#=======================================================================================================================
# The following code is for the mad-lib generator:
# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.
#=======================================================================================================================
#Key to creating a list with multiple questions is emulating sql clause aka select, update, but represented as
#functions.
#User Input Function... ask user to input what the blanks are in a sentence.
#. Show user sentence, ask to answer blanks
# Prompt user for answer to first blank
#Check to see if their answer is the same as blank. (Pass correct answer to replace[] or input?)
#If correct, recievce point * difficulty multiplier
#4 levels (Or, 4 questions)
#Easy, normal, hard (Difficulty defines number os retries and score multiplier)
# Easy = 3 tries, 1x score multiplier
# Normal = 2 tries, 1.3x score multiplier
# Hard = 1 try, 1.6 score multiplier
# score = correct/total + remaining tries * score multiplier
# When player guesses right, answer will display, if not it will ask again (removing a try)
# One way to check if correct: have blanks replaced with user input, then pass final string and compare to correct
#string.

#The colorama module is used to color output text into the terminal to give the game a little visual flair. Its also
# cross-platform. It is mostly used in the following way: print(Fore.COLOR + "TEXT" + Fore.RESET) Fore is text color,
# Back is text background, and Style is text brightness.
from colorama import Fore, Back, Style
import textwrap

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
    create_question(["banana"], ["___1___"], '''A ___1___ is yellow.''')
    create_question(["function", "variables", "values", "lists"], ["___1___", "___2___", "___3___", "___4___"],
                    '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.''')


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
    #randomPointer = random.randint(0, len(questionBank) - 1)
    #if questionBank[randomPointer] not in playedQuestions:
    #    playedQuestions.append(questionBank[randomPointer])
    #    activeQuestion = questionBank[randomPointer]
    #    return activeQuestion
    #if ran#dom_result == True:
    #activeQuestion = random.randint()


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
    #print(word)
    print(answer)
    #print()
    playerAnswer = None
    while playerAnswer != answer:
        playerAnswer = input(Fore.GREEN + "Please enter the correct answer for: " + Fore.WHITE + word + " " + Fore.RESET)
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
    #print("blank: " + str(blank))
    #print("activeQuestion[1][1]: " + str(activeQuestion[1][1]))
    #print("activeQuestion[1][0]: " + str(activeQuestion[1][0]))
    for index, item in enumerate(activeQuestion[1][1]):
        if blank == item:
            return activeQuestion[1][0][index]
        print("activeQuestion[1][0][index]: " + str(activeQuestion[1][0][index]))
        #print()
        print("item: " + str(item))
        #print(index)
        #if text_in_qs(item, blank) != None:
        #    return activeQuestion[1][0][index]


def difficulty_selector():
    """This function prompts the user to select their difficulty and describe how difficulty affects gameplay."""
    global difficulty
    playerAnswer = input(Fore.LIGHTRED_EX + "Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: " +
                         Fore.RESET)
    while playerAnswer not in ["1", "2", "3"]:
        print("Please enter the number 1, 2, or 3 for your difficulty level.")
        playerAnswer = input(Fore.LIGHTRED_EX + "Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: " + Fore.RESET)
    if playerAnswer == "3":
        difficulty_init("HARD", "3", 3, 1)
    elif playerAnswer == "2":
        difficulty_init("MEDIUM", "2", 2, 2)
    elif playerAnswer == "1":
        difficulty_init("EASY", "1", 1, 3)
    print()
    return playerAnswer


def difficulty_init(difficultyString, difficultyValue, scoreAdjuster, attemptCount):
    global scoreMultiplier
    global attempts
    global difficulty
    difficulty = difficultyValue
    attempts = attemptCount
    scoreMultiplier = scoreAdjuster
    print("You've selected " + Style.DIM + Back.RED + difficultyString + Back.RESET + ". This gives you "
          + str(attempts) + " attempt(s) to solve each question while gaining " + str(scoreMultiplier) + "x points."
          + Style.RESET_ALL)


def attempt_and_score_text():
    """This function prints out a colored graphic to the player representing their score and attempts."""
    print("(" + Fore.RED
          + "♥" * attempts + Fore.RESET + Fore.GREEN + ")" + " (" + Fore.RESET + Fore.LIGHTYELLOW_EX
          + "◎" * score + Fore.RESET + Fore.GREEN + ")" + Fore.RESET)


def test(input):
    string = input
    print(string)
    return textwrap.wrap(string, 70)


def play_game(inputString, blankSet):
    """This function compares inputString to blankSet to determine when and where to prompt the user for an answer. It
    will also mutate inputString to return a new question with its respective blanks filled as they are answered
    correctly by the player."""
    replaced = []
    stringaslist = inputString.split()
    print(Fore.GREEN + "Read the following sentence(s) and fill in the blanks when prompted... ")
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
           print(Fore.YELLOW +" ".join(replaced).replace(text, return_active_answer(text_in_qs(text, blankSet))) + Fore.RESET + " " + " ".join(stringaslist[len(replaced):]))
       else:
           replaced.append(text)



def game_controller(start=False):
    """This function serves as a wrapper to call all preceding functions. It also will not execute unless explicitly
    passed in as True."""
    load_questions()
    if start == True:
        print(Fore.YELLOW + "=" * 103 + Fore.RESET)
        print(Fore.YELLOW + " " * 28 + "Welcome to Alkarion's IPND Quiz Project!" + Fore.RESET)
        print(Fore.YELLOW + "=" * 103 + Fore.RESET)
        difficulty_selector()
        while len(playedQuestions) < len(questionBank):
            select_question()
            play_game(activeQuestion[1][2], activeQuestion[1][1])
            print()
    return None


#print(questionBank)
#print("current question index: " + str(questionIndex))
#print ("new question index: " + str(questionIndex))
#print("questionBank[0] = " + str(questionBank[0]))
#print("questionBank[1] = " + str(questionBank[1]))
#print("questionBank[1][1][2] = " + str(questionBank[1][1][2]))
#print(min(questionBank))



game_controller(True)
#print(select_question())
#print(select_question())
#print(activeQuestion)
#print(activeQuestion[1][0])
#print(activeQuestion[0][2])
#print(activeQuestion[0][2])
#print(activeQuestion[2])
#def determineAnswer(blankSet):
    #text_in_qs()

#print(return_active_answer("__1___"))

#print("max: " + str((questionBank[1])))
#print("len: " + str(len(questionBank))