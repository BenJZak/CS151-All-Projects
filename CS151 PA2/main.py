# Programmer: Ben Zakielarz
# Course:  CS151, Dr. Kenyon
# Due Date: 10/19/23
# Project Assignement: 2
# Problem Statement: Create a 3 player stick game
# Data In: Amount of sticks removed
# Data Out: Respective loss count
# Credits: N/A

#library imports
import os
import random
import time


#function that runs while the gamePhase is active, establishes properties of the game
def gamePhase(sticks):
  global computerLosses
  global playerOneLosses
  global playerTwoLosses

  #computer is easy, meaning it will pick some random number 1-3
  randRemove = random.randint(1,3)
  print("Computer goes first, it chooses to remove", randRemove, "sticks.")
  sticks -= randRemove
  #checks to see if sticks < 0 using seperate function
  if isGameOver(sticks) is True:
    print("The computer has lost!")
    computerLosses += 1
    return False
  print("-------------------------------")
  print("There are", sticks, "sticks remaining.")
  print("-------------------------------")

  while sticks >= 0:
    randRemove = random.randint(1,3)
    p1Remove = int(input("Player 1 how many sticks would you like to remove? (1-3): "))
    #checks to see if user inputted value is valid (a value 1-3)
    while p1Remove < 1 or p1Remove > 3:
      print()
      print("\t\t Invalid Entry.")
      print()
      p1Remove = int(input("Player 1 how many sticks would you like to remove? (1-3): "))
    sticks -= p1Remove
    if isGameOver(sticks) is True:
      print()
      print("Player 1 has lost!")
      playerOneLosses += 1
      return False
      break
    print("-------------------------------")
    print("There are", sticks, "sticks remaining.")
    print("-------------------------------")
    p2Remove = int(input("Player 2 how many sticks would you like to remove? (1-3): "))
    while p2Remove < 1 or p2Remove > 3:
      print()
      print("\t\t Invalid Entry.")
      print()
      p2Remove = int(input("Player 1 how many sticks would you like to remove? (1-3): "))
    sticks -= p2Remove
    if isGameOver(sticks) is True:
      print()
      print("Player 2 has lost!")
      playerTwoLosses += 1
      return False
      break
    print("-------------------------------")
    print("There are", sticks, "sticks remaining.")
    print("-------------------------------")
    time.sleep(1)
    print("Computers turn, it chooses to remove", randRemove, "sticks.")
    sticks -= randRemove
    if isGameOver(sticks) is True:
      print()
      print("Computer has lost!")
      computerLosses += 1
      return False
      break
    print("-------------------------------")
    print("There are", sticks, "sticks remaining.")
    print("-------------------------------")

#function that runs when the amount of sticks <= 0
#displays respective loss count and gives user option to play again
def endPhase():
  global gameState
  global sticks
  print()
  print("----------------------")
  print("Player 1 Losses:", playerOneLosses)
  print("Player 2 Losses:", playerTwoLosses)
  print("Computer Losses:", computerLosses)
  print("----------------------")
  print()
  gameState = input("Would you like to play again? (y/n)").strip().lower() == 'y'
  if gameState is True:
    sticks = 0
    while sticks < 10 or sticks > 100:
      sticks = int(input("How many sticks would you like to start with? (Choose any value 10-100): "))
      if sticks < 10 or sticks > 100:
        print()
        print("\t\t Invalid Entry.")
        print()
#function that checks to see if the game is over, returns T/F value
def isGameOver(sticks):
  return sticks <= 0

#clears terminal to get rid of annoying 'main.py' thing
os.system('clear')

#initializes losses per player
computerLosses = 0
playerOneLosses = 0
playerTwoLosses = 0
gameState = True

#introductory display (main menu display)
print("Welcome to the game of sticks!")
print("------------------------------")
print()
print("Rules: This is a 3 player game (one player is a computer) where each player takes turns taking 1, 2, or 3 sticks from the pile. The player who takes the last stick from the pile loses!")
print()
#initial declaration of the starting amount of sticks
sticks = 0
while sticks < 10 or sticks > 100:
  sticks = int(input("How many sticks would you like to start with? (Choose any value 10-100): "))
  if sticks < 10 or sticks > 100:
    print()
    print("\t\t Invalid Entry.")
    print()
#gameState used to check the state of the game
while gameState is True:
  #while the player is in the gamePhase, gamePhase executes, otherwise it moves onto endPhase
  while True:
    if gamePhase(sticks) is True:
      gamePhase(sticks)
    else:
      break
  #executes endPhase function while it is True
  while True:
    if endPhase() is True:
      endPhase()
    else:
      break
  #otherwise (and after gameState is no longer True) print the final text scrn
print("----------------------")
print()
print("Thanks for playing!!")
  