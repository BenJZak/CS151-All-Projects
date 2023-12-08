# Programmers: Ben Zakielarz
# Course: CS151, Dr. Kenyon
# Due Date: 11/21/2023
# Project Assignment: 4
# Problem Statement: You are creating a to analyze headlines from the Australian Broadcasting Company (ABC). Your program is going to read in the file chosen by the user, and then allow them to request specific types of analysis on that file.
# Credits: https://developers.google.com/edu/python/sorting - found key=len throug this site
#Another Credit: https://www.geeksforgeeks.org/with-statement-in-python/ - used for with statement

#Function name:  averageChars
#Purpose: Determines the average amount of characters in given  files
#Parameters: files to analyze
#Return: average amount of chars 
def averageChars(files):
  total_chars = 0
  total_headlines = 0
  #I know we haven't used it, but im sure you know that "with" can be used to simplify file management as it will automatically close the file after done being mutated
  for file in files:
    try:
      with open(f"{file}.txt", "r") as f:
        headlines = f.readlines()
        total_chars += sum(len(headline) for headline in headlines)
        total_headlines += len(headlines) #calculations
    except FileNotFoundError:
      print(f"File {file}.txt not found.") #Error checking contained within each function just in case

  if total_headlines == 0:
    return 0  #avoids division by zero erros

  avg_chars = total_chars / total_headlines
  return avg_chars

#Function name: writeNew
#Purpose: writes a new file all the headlines that are contained within files, name determined by user
#Parameters: files and word to search for within them
#Return: a new file 
def writeNew(files, word):
  new_file_name = input("Enter the name for the new file (without .txt extension): ").strip()
  new_file_name += ".txt"  #add the extension to avoid user being dumb
  try:
    with open(new_file_name, "w") as new_file:
      #iterate thru files given
      for file in files:
        try:
          with open(f"{file}.txt", "r") as f:
            #read all headlines from files
            headlines = f.readlines()
            #filter all those headlines using the given word
            matching_headlines = [headline.strip() for headline in headlines if word.lower() in headline.lower()]
            #writes it into a new file
            for matching_headline in matching_headlines:
              new_file.write(matching_headline + "\n")
        except FileNotFoundError:
          print(f"File {file}.txt not found.")
    #notifies that a new file was successfully created whippee
    print(f"New file '{new_file_name}' created with headlines containing '{word}'.")
  except Exception as e:
    print(f"Error creating the new file: {e}")
    #this functtion takes a lot of error checking

#Function name: determineHeadlines
#Purpose: determines how many times a word occurrs in each headline
#Parameters: files and word to search for
#Return: the num of times a word occurrs in each headline
def determineHeadlines(files, word):
  results = {}
  #go thru files blah blah blah
  for file in files:
    try:
      #open file using with
      with open(f"{file}.txt", "r") as f:
        #read into variable
        headlines = f.readlines()
        #check for the word you know the deal
        count = sum(1 for headline in headlines if word.lower() in headline.lower())
        results[file] = count
    except FileNotFoundError:
      print(f"File {file}.txt not found.")

  return results

#Function name: longestHeadline
#Purpose: determines the longest headline
#Parameters: files
#Return: the longest headline of given files
def longestHeadline(files):
  longest_headline = ""
  #do i even have to say it again
  for file in files:
    try:
      #im sure we get the idea
      with open(f"{file}.txt", "r") as f:
        #cmon now
        headlines = f.readlines()
        if headlines:
          #find the longest headline in the current file
          current_longest = max(headlines, key=len) #ken=len compares strings based on length rather than their lexicographic order
          #update the overall longest headline if the current one is longer
          longest_headline = max(longest_headline, current_longest, key=len)
    except FileNotFoundError:
      print(f"File {file}.txt not found.")

  return longest_headline

#Function name: main
#Purpose: controlls general operations and directing to files
#Parameters: none
#Return: none
def main():
  count = 0
  files = []
  option = ""
  while count < 6 or option != "exit":
    option = input("2014\n2015\n2016\n2017\n2018\n2019\nInput the year of headlines you would like to analyze or type exit: ").strip().lower()
    while option != "2014" and option != "2015" and option != "2016" and option != "2017" and option != "2018" and option != "2019" and option != "exit":
      print("\nInvalid Entry\n")
      option = input("2014\n2015\n2016\n2017\n2018\n2019\nInput the year of headlines you would like to analyze or type exit: ").strip().lower()
    while files.__contains__(option):
      print("\nAlready Requested Operand\n")
      option = input("2014\n2015\n2016\n2017\n2018\n2019\nInput the year of headlines you would like to analyze or type exit: ").strip().lower()
    if option != "exit":
      files.append(option)
    else:
      count = 100
  operand = input("\n1. How many headlines contains a particular word\n2. Write to a new file all headlines that have a particular word in it\n 3. Determine average number of characters per headline\n4. Output longest headline in a file\n5. Read in a new file to analyze\n Enter the number of which operand you would like to perform: ").strip()
  while operand != "1" and operand != "2" and operand != "3" and operand != "4" and operand != "5":
    print("\nInvalid Input\n")
    operand = ("\n1. How many headlines contains a particular word\n2. Write to a new file all headlines that have a particular word in it\n 3. Determine average number of characters per headline\n4. Output longest headline in a file\n5. Read in a new file to analyze\n Enter the number of which operand you would like to perform: ").strip()
  quit = False
  if operand == "1":
    word = input("What word would you like to search for?: ").strip()
    result = (determineHeadlines(files, word))
    print(f"Number of headlines containing '{word}': {result}")
    print(f"\n\tCurrent files being analyzed: {files}\n")
    quit = input("Would you like to quit the program? Y/N: ").strip().lower() == 'y'
    if quit == True:
      print("\n\tThank you for using the program!")
      exit() #I'm sorry I'm using this but it works so well in this case and doing it another way would be too complicated for me  :(
    main()
  if operand == "2":
    word_to_search = input("What word would you like to search for?: ").strip()
    writeNew(files, word_to_search)
    print(f"\n\tCurrent files being analyzed: {files}\n")
    quit = input("Would you like to quit the program? Y/N: ").strip().lower() == 'y'
    if quit == True:
      print("\n\tThank you for using the program!")
      exit()
    main()
  if operand == "3":
    result = averageChars(files)
    print(f"Average number of characters per headline: {result}")
    print(f"\n\tCurrent files being analyzed: {files}\n")
    quit = input("Would you like to quit the program? Y/N: ").strip().lower() == 'y'
    if quit == True:
      print("\n\tThank you for using the program!")
      exit()
    main()
  if operand == "4":
    result = longestHeadline(files)
    print(f"Longest headline: {result}")
    print(f"\n\tCurrent files being analyzed: {files}\n")
    quit = input("Would you like to quit the program? Y/N: ").strip().lower() == 'y'
    if quit == True:
      print("\n\tThank you for using the program!")
      exit()
    main()
  if operand == "5":
    files = []
    print("\n\tFiles Cleared\n")
    print(f"\n\tCurrent files being analyzed: {files}\n")
    quit = input("Would you like to quit the program? Y/N: ").strip().lower() == 'y'
    if quit == True:
      print("\n\tThank you for using the program!")
      exit()
    main()
main()
