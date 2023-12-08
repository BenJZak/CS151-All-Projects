# CS151 PROGRAMMING ASSIGNMENT #4

* Design grade: MRN
* Programming Grade:  EMRN                                 			
* DESIGN DUE: Friday 11/10/23 at 11:59PM
* FINAL DUE: Tuesday 11/21/23 at 11:59PM

Note: PA is due last day before break to give you flexibility on when you complete it, but you can finish it before then if you want to get it done; you already know everything you need to know to do this lab.

## I. PROBLEM:

You are creating a to analyze headlines from the Australian Broadcasting Company (ABC). Your program is going to read in the file chosen by the user, and then allow them to request specific types of analysis on that file. The headlines included in this assignment are real headlines from this real news agency.

## II. PURPOSE OF THE ASSIGNMENT

The purpose of this assignment is to give you  
1. Practice with files
2. Practice with lists
3. Practice with designing functions
4. Practice with implementing functions

## III. REQUIREMENTS ANALYSIS 

The first stage in your programming assignment is the requirements analysis stage.  You must understand the problem before you can try to solve it.

At the start of the program, the user will get to tell you the name of a headline file they would like to analyze. You must read in this data and store it in a list before doing any analysis. Your program should have excellent usability and prevention of crashing.

### Files

Included in this assignment are six potential input files, all of the same format, but with different data. If you write your code correctly, it will be able to read in any of the files and process it without changing any of your code.

Each file has 1 headline per line of the file. The files are very large, which is one of the reasons we need Python to help us analyze them.

### Usability
Your program must have excellent usability, including error checking. It should be clear what to input, and error checking should prevent the user from crashing your program.

### User Options

The user can choose the following types of analyses on the file they chose to analyze at the start of the program:

1. Determine how many headlines have a particular word in it, for a single file
2. Write to a new file all headlines that have a particiular word in it. User gets to choose the name of the new file.
3. Determine the average number of characters per headline
4. Output the longest or shortest headline (you choose which one you want to design your program to do!). Length is determined by number of characters.
5. Read in a new file to analyze. If the user chooses this option, it overwrites the data you had been storing (e.g. old file is no longer stored in program after new file is read in)

The user gets to keep choosing what they want to do until they choose to quit.

## IV. DESIGN

The second stage is to design your solution based on the requirements. Think about how to break the problem up into different smaller problems that are easier to solve. In particular, what functions do you need? Remember that functions are the tasks that the program is solving.

For this design, you need to determine the functions that you need and their algorithms. For each function you need to know:
```
Function name:
Purpose:
Parameters:
Return:
Algorithm:
```

Don't forget main and error checking!


### DESIGN SUBMISSION: 11/10/23

Submit To Moodle a Word document containing a list of planned functions in the above format, including an algorithm for each function.


## V. PROGRAMMING REQUIREMENTS

After your design is complete and correct, it’s time to start programming and then testing. This is a great time to start practicing iterative development. Instead of writing an entire program and then testing it, write part of it, test it, then write the next part. That way if something is broken it will be easier to figure out why. Now that you have functions, there are natural ways to build up a working program. For example, get the basic menu functionality working, where you just output what each option does. Then, add file reading. Make sure that works, then add in an analysis option, etc.

**Be careful not to overwrite the contents of your input files. Never use your input file as the name of your output file**. If you accidentally do this, you can use the history functionality at the bottom of this view to revert the text file to its original data.

Remember that your program should:
1. Follow good usability/HCI principles in input and output. You must go above and beyond what we were doing in the first half of the semester, now that we know how to special characters like tabs, and f strings for print formatting.
2. Protect the program against bad user input
3. State at the start the purpose of the program.

### Testing your Program

To make it easier to test your program, we provide a few of the expected answers. The below does not include error checking, and you probably want to run it for other inputs as well.

For 2017.txt:
* the word "cat" appears 34 times
* the word "pirate" appears 4 times
* the average number of words in a headline is 49.5

For testing files it can also be useful to test on a smaller file that you can easily check by hand against. We've provided testfile.txt for this purpose. Here you can figure out which lines should be included for whatever word you are searching for, or calculate what the average length should be, and compare to what your program is doing.

### To earn an E
If you are going for an E on this assignment, it should have most of the following:
1. Works correctly
2. Has good commenting
3. Uses for loops
4. Overall good code style and choices
5. Excellent usability


## VII. ASSIGNMENT REMINDERS

Follow the programming assignment requirements document for comments, formatting, etc. Follow the honor code guidelines outlined in the syllabus and at https://www.loyola.edu/academics/computer-science/current-students/honor-code.

**Remember to ask for help early if you are stuck -- don't wait until the night before it's due to start asking for help.**

## VIII. REFLECTION

Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult? Was anything easier than expected?  What was it like designing with functions and using files with lists? This should be no more than a page.

## IX. FINAL SUBMISSION due 11/21/23

1. To Replit:  
    1. Your main.py file    
    2. Your reflection of the programming assignment in reflection.txt. Remember to follow the prompts above.
2. To Moodle:    
    1. Your final algorithms in Word, including the changes you made based on the design feedback.

***Remember to submit your replit project.***
