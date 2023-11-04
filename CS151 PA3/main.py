# Programmers: Ben
# Course:  CS151, Dr. Kenyon
# Due Date: 11/3/23
# Project Assignment: 3
# Problem Statement: You are creating a program to display ASCII art and string decorations to the user. ASCII art is just a combination of characters that make a design or pattern.
# Data In: numbers that coorespond to their respective functions being called
# Data Out: ASCII art
# Credits: ChatGPT and https://www.asciiart.eu/image-to-asci

import random

#Function name: circle
#Purpose: prints a circle
#Parameters: none
#Return: a circle

def circle():
  print()
  print("             ************")
  print("          ****************")
  print("        ********************")
  print("       **********************")
  print("      ************************")
  print("      ************************")
  print("      ************************")
  print("       **********************")
  print("        ********************")
  print("          ****************")
  print("            ************")
  print()
  main()

#Function name: setOfLines
#Purpose: prints a set of lines
#Parameters: amount of lines to draw, the character its comprised of, and how many times per line to print each character
#Return: a set of lines based on user input

def setOfLines(linesToDraw, char, repeat):
  count = 0
  while count < linesToDraw:
    print(char*repeat)
    count += 1
  main()

#Function name: randomDesign
#Purpose: prints a randomDesign based off of 3 ASCII images I created
#Parameters: none
#Return: a random design based off of 3 possible print sequences

def randomDesign():
  randomNum = random.randint(1,3)
  if randomNum == 1:
    triangle = ""
    for i in range(6):
        spaces = " " * (5 - i)
        stars = "*" * (2 * i - 1)
        triangle += spaces + stars + "\n"
    print(triangle)
  elif randomNum == 2:
    #CREDIT TO CHAT GPT FOR THE SMILEY FACE CONCEPT (I modified it heavily though)
    smiley = """
     .---------.
    /  o    o  \\
    |    ∆    |
    |  \___/  |    Hello :D
    '-_______-'
    """
    print(smiley)
  else:
    #CREDIT TO https://www.asciiart.eu/image-to-ascii
    hehehe = """
                  ..:=*######%%%%%%%######**++=--:......                    
                 :%@%=:..........::--------::::-=+*##%@@@@@#=:.             
               :%@=.       :=+-.  ....::...   .............:=*@@%-.         
              =@*.      -+:.:+=-:..       ..:------------:..:=..-#@%:       
             *@=.    -=..==.:*+::......+:.        .:=+++++*:      .:@%.     
            +@=    :. .#.:#.            =:         :.       .#.     .@%.    
          .+@=       :..+.  ..::--::..   .        .-          -      *@.    
         .%@=            :#@@@@@@@#*%@@+.         .. .:-===-:.       :@#.   
       .%@@*=-:..  .==:.#@+*@@@@@@*-. .+@%.       .+@@@@@%%@@@-:-:.....*@%. 
     .#@+*:...-==-:...+.:==-:..-::-*@@%#@@.    -@@@@@@%*+--::..      .=-.*@=
    :@%-=. =@@*-::*@@@+.    :%@%.    ..+..      .:@+.          .:--:..#.--%%
    %%.- .*@:  .+%.  .=#@@@@%-.                  .@#.    .#*:=@@*--*@%.= -*@
    @. - :@=  .-@@@%=.             ...:--.        -@@+.   .=*#*..#.   .+ -*@
    @- - :@==@@@@=.:*@@#=..  .======.@%=-.          .@@@-.      =@*. .*:.#@#
    #@.-: #%   .%@:   .=@@@@#=..    .@*.*@@@@*     .+@%%--+=   .%@@+ .:*-#@:
    .@@:-+...  .+@@@+.  *@..:+@@@@%=..+...     :%+*@%..    ...#@@#@%... *@: 
     .*@%:...    :@@#@@@@@@:.     :@@@@@@%+:.....::......:*@@@@@=@@@. .=@-  
       .%@=.      .%@-.:%@@@@@+:. :@+   ..-#@@%%@@@@@@@%%%@#  *@.#@@: .#%.  
         -@#.       +@*.=@:-#@@@@@@@=:.     #%    .@*     #% .%@@@@@: .#%   
          :@@.       .%@@%.   .:=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. .##   
           :@%.       .:%@*.     =@-.:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@%. .#%   
            .%@:         .#@@-  :@#.      :@+-+#%@@@@@@@@@@@@@+@@*@-  .#%   
              =@@:...  ..   :%@@@@.       :@-    .@%.  =@:.*@--@*@+.  .#%   
               .=@@=.=+:.:+-.  .+%@@@*=-:.=@-    :@= .=@#.=@%#@@#:    .*%.  
                 .:#@%=.:=+..-==.   .:-=*#%%@@@@@@@@@@@@%#*=-:.       .*@.  
                    .:#@@*..:=+:.:=+:.        .........       .-=.  .  +@.  
                       ..=@@@*....=*-..-**+-:...           .+*:.   --  -@:  
                            .=%@@*:.   ..-+*+:..........      ..:*:.   :@-  
                                .=%@@+:.             ...........      .@%.  
                                    .=%@@#*=-.                      .=@#.   
                                        .:-=*@@@@%*-..           .=%@%:.    
                                               ...:=*%@@@@@@@@@@%#=..       
    """
    print(hehehe)
  main()

#Function name: main
#Purpose: handles the inputs of the user and directing their choices to call respective functions
#Parameters: none
#Return: nothing technically

def main():
  print("1. Circle\n2. A set of lines\n3. A random design\n")
  designChoice = str(input("Please enter a number based on what design you would like to print. Or print 'stop' to end the program: ")).strip().lower()
  #makes sure user inputs one of four possible valid inputs
  while designChoice != "1" and designChoice != "2" and designChoice != "3" and designChoice != "stop":
    print("\nInavlid Input\n")
    designChoice = str(input("Please enter a number based on what design you would like to print. Or print 'stop' to end the program: ")).strip().lower()
  if designChoice == "1":
    circle()
  elif designChoice == "2":
    linesToDraw = input("How many lines would you like to draw?: ")
    #makes sure user inputs a integer and not a float value or string
    while (not linesToDraw.isdigit()) or linesToDraw.__contains__("."):
      print("\nInavlid Input - Must be Integer\n")
      linesToDraw = input("How many lines would you like to draw?: ")
    linesToDraw = int(linesToDraw)
    char = input("What character would you like to make the line out of?: ").strip()
    repeat = input("How many times would you like to have the character repeat per line?: ")
    while (not repeat.isdigit()) or repeat.__contains__("."):
      print("\nInavlid Input - Must be Integer\n")
      repeat = input("How many times would you like to have the character repeat per line?: ")
    repeat = int(repeat)
    setOfLines(linesToDraw, char, repeat)
  elif designChoice == "3":
    randomDesign()
  elif designChoice == "stop":
    print("\nThanks for checking out this program!")

print("This program is designed to display ASCII art based on your inputs!\n")
main()
