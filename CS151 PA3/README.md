# CS151 PROGRAMMING ASSIGNMENT #3

* Design grade: MRN
* Programming Grade:  EMRN                                 			
* DESIGN DUE: Thursday 10/27/23 at 11:59PM
* FINAL DUE: Thursday 11/03/23 at 11:59PM

## I. PROBLEM:

You are creating a program to display ASCII art and string decorations to the user. ASCII art is just a combination of characters that make a design or pattern.

## II. PURPOSE OF THE ASSIGNMENT

The purpose of this assignment is to give you  
1. Practice with protecting against bad user input
2. Practice with decision making
3. An opportunity to use looping
4. Practice with designing functions
5. Practice with implementing functions
6. A chance to be creative

## III. REQUIREMENTS ANALYSIS 

The first stage in your programming assignment is the requirements analysis stage.  You must understand the problem before you can try to solve it.

Your program must give the user three design options, and allow them to keep choosing options and seeing the output from their choice until they've chosen to stop: Outputting a circle, outputting a set of lines, or outputting a random design. Each of those options have further requirements below. Your program must be implemented such that all of your code is in functions, where each function solves one task.

### Outputting  a circle
How can you make a circle? This shape will be more an approximation of a circle using slashes, underscores, and/or dashes. Don't overthink it; this part shouldn't be too hard, just figure out how to output the right characters to make what basically looks like a circle on the screen.

### Outputting a set of lines
The user gets to decide three things each time they choose an option:

1. How many lines to draw. The lines are drawn directly after each other, on a new line.
2. What character or set of characters are repeated to make the line
3. How many times to repeat the character(s) for the line

For example, if the user chooses to output 3 lines that use "*" that is repeated 20 times, the output will look like:
```
********************
********************
********************
```

### Random design
You must create three different designs to be displayed. When the user chooses this option, your program will randomly choose which of the three designs to output. 

For your three designs, they must be substantially different from the circle and line requirements. You can, however, get inspiration from elsewhere. Here are the rules:

1. **At most one design may be an ASCII art you find online**, even if it includes the python code to generate it. *You MUST put a comment with exactly where you got it from if you go this route, otherwise it is plagiarism.*
2. **Your other two designs can be entirely your own creation or inspired by art you find elsewhere.** However, you *may NOT look up the code for how to create them*; you must try to figure it out yourself. You can use string functionality, loops, etc. If you get inspiration from elsewhere, credit that inspiration in your code in a comment!
3. **At least one of your designs must do something other than just writing out the art line by line**; for example it may have a loop, use the `*` symbol to replicate a string, or use a string function call.

### Usability
Your program must have excellent usability, including error checking. It should be clear what to input, and error checking should prevent the user from crashing your program.

## IV. DESIGN

The second stage is to design your solution based on the requirements. Think about how to break the problem up into different smaller problems that are easier to solve. In particular, what functions do you need? Remember that functions are the tasks that the program is solving.

For this design, you need to determine the functions that you need. For each function you need to know:
```
Function name:
Purpose:
Parameters:
Return:
```

For the main function, you also need an algorithm for what the high level steps of the algorithm will be. If you need to call a function, saying something like "Call the XXX function with arguments Y, Z" (if a function was named XXX and you had values Y and Z you were planning to send as arguments, e.g. `XXX(Y,Z)`).

You also should figure out the basic plan for at least one if not all three of your random designs, and include that in your design submission.


### DESIGN SUBMISSION: 10/27/23

Submit To Moodle a Word document containing:

1. list of planned functions in the above format, with an Algorithm for the main function.
2. Your basic plan for at least one of your random designs -- either what you want to design, the source you've found for inspiration, your algorithm, or something similar.

## V. PROGRAMMING REQUIREMENTS

After your design is complete and correct, it’s time to start programming and then testing. This is a great time to start practicing iterative development. Instead of writing an entire program and then testing it, write part of it, test it, then write the next part. That way if something is broken it will be easier to figure out why. Now that you have functions, there are natural ways to build up a working program. For example, get the basic menu functionality working, where you just output what each option does. Then, add in one design (say, the circle). Make sure that works, then add in the code for the lines. Then start adding in the three option designs. This way, you have a working program after each addition, and can test if it's right before you move on to the rest of the code.

Remember that your program should:
1. Follow good usability/HCI principles in input and output. You must go above and beyond what we were doing in the first half of the semester, now that we know how to special characters like tabs, and f strings for print formatting.
2. Protect the program against bad user input
3. State at the start the purpose of the program.

## VII. ASSIGNMENT REMINDERS

Follow the programming assignment requirements document for comments, formatting, etc. Follow the honor code guidelines outlined in the syllabus and at https://www.loyola.edu/academics/computer-science/current-students/honor-code.

**Remember to ask for help early if you are stuck -- don't wait until the night before it's due to start asking for help.**

## VIII. REFLECTION

Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult? Was anything easier than expected?  What was it like designing with functions? This should be no more than a page.

## IX. FINAL SUBMISSION due 11/03/23

1. To Replit:  
    1. Your main.py file    
    2. Your reflection of the programming assignment in reflection.txt. Remember to follow the prompts above.
2. To Moodle:    
    1. Your final algorithms in Word, including the changes you made based on the design feedback.

***Remember to submit your replit project.***
