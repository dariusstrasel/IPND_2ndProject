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

#Todo: function which controls flow of game? 1.Introduction 2. Question set 3.Score/conclusion stub
#Todo: score stub
#-----> leaderboard?
#Todo: display question/answer stub
#Todo: difficulty (with score modifier, and "try" count stub
#Todo: lose/win stub
#Todo: modify question iterator to select a question index from bank instead of single variable
#Todo: Add userinput prompt
#Todo: Determine how to replace blank with the correct answer and not "corgi"
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
import random

activeQuestion = 0
questionIndex = 0
difficulty = 1
uniqueIDList = []
playedQuestions = []
questionBank = []
#questionGroup = [qsID[[question][answer]]]
#global questionIndex

blankSet = ["___1___", "___2___", "___3___", "___4___"]
questionAnswer = ["function", "variables", "values", "lists"]
questionString = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


def assign_unique_id():
    """Docstring"""
    global questionIndex
    global uniqueIDList
    if questionIndex not in uniqueIDList:
        uniqueIDList.append(questionIndex)
        return questionIndex
    questionIndex = questionIndex + 1
    uniqueIDList.append(questionIndex)
    return questionIndex


def select_question(random=False):
    """Docstring"""
    global playedQuestions
    global activeQuestion
    if random == True:
        activeQuestion = random.randint()
    #if activeQuestion not in playedQuestions:


def load_questions():
    """Docstring"""
    createQuestion(["banana"], ["___1___"], '''A ___1___ is yellow.''')
    createQuestion(["function", "variables", "values", "lists"], ["___1___", "___2___", "___3___", "___4___"],  '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.''')


def player_input():
    """Docstring"""
    playerAnswer = input("Please enter the correct answer for the blank: ")
    return playerAnswer


def create_question(questionAnswer, blankSet, questionString):
    """Docstring"""
    qsGroup = [assignUniqueID()]
    qsGroup.append([questionAnswer, blankSet, questionString])
    questionBank.append(qsGroup)


def text_in_qs(word, blankSet):
    """Docstring"""
    for tiq in blankSet:
        if tiq in word:
            return tiq
    return None


def difficulty_selector():
    """Docstring"""
    global difficulty
    playerAnswer = input("Please select your difficulty: (1) Easy, (2) Normal, (3) Hard: ")
    if playerAnswer == 3:
        difficulty = 3
    elif playerAnswer == 2:
        difficulty = 2
    elif playerAnswer == 1:
        difficulty = 1


def play_game(inputString, blankSet):
    """Docstring"""
    replaced = []
    stringaslist = inputString.split()
    for text in stringaslist:
       if text_in_qs(text, blankSet) != None:
           replaced.append(text.replace(text_in_qs(text, blankSet), playerInput()))
       else:
           replaced.append(text)
    return " ".join(replaced)


def game_controller(start=False):
    """Docstring"""
    loadQuestions()
    if start == True:
        print("Welcome to Alkarion's IPND Quiz Project!")
        difficultySelector()
        play_game(questionString, blankSet)
    return None


#print(questionBank)
#print("current question index: " + str(questionIndex))
#print ("new question index: " + str(questionIndex))
#print("questionBank[0] = " + str(questionBank[0]))
#print("questionBank[1] = " + str(questionBank[1]))
#print("questionBank[1][1][2] = " + str(questionBank[1][1][2]))
#print(min(questionBank))

game_controller(True)