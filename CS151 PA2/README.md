# CS151 PROGRAMMING ASSIGNMENT #2

* Design grade: MRN
* Programming Grade:  EMRN                                 			
* DESIGN DUE: Thursday 10/12/23 
* FINAL DUE: Thursday 10/19/23

## I. PROBLEM:

You are creating a three player game of the Game of Sticks. In this game there is a pile of sticks on the table, and players alternate turns taking 1-3 sticks. The player to take the last stick loses.

## II. PURPOSE OF THE ASSIGNMENT

The purpose of this assignment is to give you  
1. Practice with protecting against bad user input
2. Practice with decision making
3. An opportunity to use looping
4. A chance to be creative

## III. REQUIREMENTS ANALYSIS 

The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the game. The rules are as follows:
1.	The game starts with some number of sticks on the table (between 10 and 100, chosen by the user)
2.	Three players take turns choosing how many sticks to take.
3.	On each player’s turn they must take either 1, 2, or 3 sticks.
4.	The player to take the last stick loses.

For your game, the following must be true:
1. **One of your players is the program itself** (e.g. a computer player you play against); the other two players are humans sitting at the computer together. The computer player chooses a random number of sticks within the valid range (1-3).
2. You must keep track of **how many times** each player loses the game
3. After the game ends, you must **ask the user if they want to play again**. If so, the game resets. However, you still keep track of losses across all games.
4. After the user decides they are ready to quit at the end of a game, you must **output how many times each player lost**.
5. You must have **error checking loops** on the types of values the user is inputting. What values are the user inputting, and what could make them invalid?
6. You must have good HCI -- the user should know what is happening, even on the computer's turn!

## IV. DESIGN

The second stage is to design your solution based on the requirements. Think about how to break the problem up into different smaller problems that are easier to solve. I recommend thinking through and developing your algorithm using these smaller versions:

1. At first, completely ignore the fact that you get to play again. Only after you've figured out the rest do you add that in. Instead, first think through a basic game of three human players, with no error checking.
2. After you've figured that out, add in error checking.
3. Now, how do you make it so that one player is the computer? What is the computer's steps? Incorporate this into your algorithm. HINT: choose which of the three players is always the computer. The computer will choose randomly among the valid stick counts.
4. Now, keep track of how many losses each player has. How do you do that?
5. No, add in the ability to play again with error checking.

If you work through each part of the algorithm and slowly build it up, in the end you'll have the full program. This is called iterative development, and is a key skill to develop for solving problems. Don't stress about how you code it -- an algorithm is a time to think through the logic without stressing about code syntax.


### DESIGN SUBMISSION: 10/12/23

Submit to Moodle: 
1. A Word document including your developed algorithm, followed by a brief description of what aspects of the assignment you think you've correctly included and what you are not sure is correct or got stuck on. This description is important as it helps make it clear that you understand what you've done, or where you need the most help in getting ready to write the code.

Your algorithm should follow the requirements of an algorithm, and contain all of the requirements for this assignment. **There should not be any code.**

## V. PROGRAMMING REQUIREMENTS

After your design is complete and correct, it’s time to start programming and then testing. This is a great time to start practicing iterative development. Instead of writing an entire program and then testing it, write part of it, test it, then write the next part. That way if something is broken it will be easier to figure out why. Use the design guidelines to help you think through the order to implement and test.

Remember that your game should:
1. Follow good usability/HCI principles in input and output. Be particularly mindful about what type of output is necessary for the user to understand what is going on in the game.
2. Protect the program against bad user input
3. State at the start the purpose of the program and how to play the game.

**Hint on random numbers:** To create a random number in Python use the method randint(a,b). It gives you a number randomly chosen in the range a<= number <=b. For instance, if you write:
	`choice = randint(10,50)`
The variable choice now holds a value that is `>=10` and `<=50`. It is called a random number because the value you get will vary within that range if you call it many times in a row (To use this function you must `import random`).

Complete a flowchart on your game to submit. Use the process of drawing the flowchart as a chance to pay attention to if the logic of your game makes sense. Use the flowchart to help you determine how to test your code, but you do not need to submit the test cases.

## VII. ASSIGNMENT REMINDERS

Follow the programming assignment requirements document for comments, formatting, etc. Follow the honor code guidelines outlined in the syllabus and at https://www.loyola.edu/academics/computer-science/current-students/honor-code.

## VIII. REFLECTION

Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult? Was anything easier than expected?  What was it like creating a more complicated game where the user can play against the computer? This should be no more than a page.

## IX. FINAL SUBMISSION due 10/19

1. To Replit:  
    1. Your main.py file    
    2. Your reflection of the programming assignment in reflection.txt.
2. To Moodle:    
    1. Your flowchart
    2. Your final algorithms in Word, including the changes you made based on the design feedback.

***Remember to submit your replit project.***
