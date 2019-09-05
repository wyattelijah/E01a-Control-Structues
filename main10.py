#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
colors = ['red','orange','yellow','green','blue','violet','purple']
play_again = ''
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #making the loop run until play_again == 'n' or 'no'
    match_color = random.choice(colors) #assigns match_color to one of the colors in the list colors
    count = 0 #sets count to be 0 initially
    color = '' #sets color to an empty string initially
    while (color != match_color): #creates a loop inside the first loop that will run until color == match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #forces color to be lowercase and have no spaces
        count += 1 #ups count by one
        if (color == match_color): #checks to see if color matches match_color
            print('Correct!') #prints 'Correct!' if line 21 is true
        else: #executes this if line 21 is false
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints 'try again' and how many times you have guessed
    print('\nYou guessed it in {0} tries!'.format(count)) #prints how many times it took you to guess correctly
    if (count < best_count): #checks to see if count is less than best_count
        print('This was your best guess so far!') #prints the statement if line 26 is true
        best_count = count #sets best_count equal to count
    play_again = input("\nWould you like to play again? ").lower().strip() #assigns play_again to user input and makes it lowercase with no spaces
print('Thanks for playing!') #prints the statement once user stops playing