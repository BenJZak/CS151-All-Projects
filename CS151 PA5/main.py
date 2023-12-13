# Programmers: Ben + Andrew
# Course:  CS151 Dr. Kenyon 
# Due Date: 12/11/23
#PA: 5
# Problem Statement: In this assignment you will create a program that organizes Pokemon for the user.
# Input Files: pokmndf.csv
# Credit: https://www.w3schools.com/python/ref_func_any.asp

# Purpose: reads in the data from pokmndf.csv file and returns it as a list of lists
# Parameters: NA
# Return: list of lists
def read_data_file():
  data_list = []

  with open("pokmndf.csv", 'r') as file:
    for line in file:
      elements = line.strip().split(',') #comma-delimited
      '''
      iterates thru each element "e" and checks if its a digit, where it will then be converted into an integer otherwise it will remain the same
      '''
      elements = [int(e) if e.isdigit() else e for e in elements]
      #append the elements to the data list
      data_list.append(elements)

  return data_list

# Purpose: filters and writes names of pokemon to a new file
# Parameters: data_list from prev func, two pokemon types, and the name of an output file
# Return: filtered names list
def filter_and_write_names(data_list, type1, type2, output_file):
  filtered_names = []
  
  with open(output_file, 'w') as output:
    for element in data_list:
        #checks to see if either type 1 or type 2 is present in the element
      if any(i in str(item) for i in [type1, type2] for item in element):
        #append the Pokemon name to the filtered_names list
        filtered_names.append(element[1])
        output.write(element[1] + '\n')  
  
  return filtered_names

# Purpose: calculates hp percentages of pokemon
# Parameters: datalist from prev func
# Return: low, med, and high hp in percentage form
def calculate_hp_percentage(data_list):
  #initialize vars
  low_hp_count = 0
  medium_hp_count = 0
  high_hp_count = 0

  for element in data_list:
    #the 7th element in the dataset is the pokemon's HP statistic
    hp_statistic = element[6]
    #basic logic
    if hp_statistic < 50:
      low_hp_count += 1
    elif 50 <= hp_statistic <= 125:
      medium_hp_count += 1
    else:
      high_hp_count += 1

  total_pokemon = len(data_list)

  #calculate percentages
  low_hp_percentage = (low_hp_count / total_pokemon) * 100
  medium_hp_percentage = (medium_hp_count / total_pokemon) * 100
  high_hp_percentage = (high_hp_count / total_pokemon) * 100

  return low_hp_percentage, medium_hp_percentage, high_hp_percentage

# Purpose: finds which pokemon has the highest attack increase
# Parameters: data list from data read func
# Return: all pokemon that have the highest attack increase
def highest_attack_increase(data_list):
  max_increase = 0
  pokemon_with_max_increase = []
  
  for element in data_list:
    #the 8th element is the basic attack and the 10th element is the special attack
    basic_attack = element[7]
    special_attack = element[9]
  
    attack_increase = special_attack - basic_attack
  
    #check if the current Pokemon has a higher attack increase
    if attack_increase > max_increase:
      max_increase = attack_increase
      pokemon_with_max_increase = [element[1]]  #save the Pokemon's name
    elif attack_increase == max_increase:
      pokemon_with_max_increase.append(element[1])  #add another Pokemon with the same increase
  
  return pokemon_with_max_increase, max_increase

# Purpose: finds which pokemon weighs the most
# Parameters: data list
# Return: the fattest pokemon
def fattest_pokemon(data_list):
  max_weight = 0
  fattest_pokemon_list = []

  for element in data_list:
      #the 4th element is the Pokemon's weight
      weight = element[3]

      #check if the current Pokemon has higher weight
      if weight > max_weight:
          max_weight = weight
          fattest_pokemon_list = [element[1]]  #aave the Pokemon's name
      elif weight == max_weight:
          fattest_pokemon_list.append(element[1])  #add another Pokemon with the same weight

  return fattest_pokemon_list, max_weight

# Purpose: performs routing and general operations
# Parameters: na
# Return: na
def main():
  choice = input("Choose what you would like to do:\n1. Filter pokemon by type\n2. See what percentage of Pokemon have a low, medium, or high HP\n3. Which pokemon(s) have the highest increase in attack\n4. Which pokemon is the fattest\n5. Exit program\n").strip()
  while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
    print("\n\tMust input an integer value within 1-5\n")
    choice = input("Choose what you would like to do:\n1. Filter pokemon by type\n2. See what percentage of Pokemon have a low, medium, or high HP\n3. Which pokemon(s) have the highest increase in attack\n4. Which pokemon is the fattest\n5. Exit program\n").strip()
  if choice == "1":
    print("Normal, Fire, Water, Grass, Flying, Fighting, Poison, Electric, Ground, Rock, Psychic, Ice, Bug, Ghost, Steel, Dragon, Dark, Fairy")
    type1 = input("\nChoose a type of Pokemon: ")
    type2 = input("\nChoose another type of Pokemon: ")
    result = filter_and_write_names(read_data_file(), type1, type2, "sortedpokemon.txt")
    print(result)
  if choice == "2":
    hp_percentages = calculate_hp_percentage(read_data_file())
    print(f"Percentage of Pokemon with low HP: {hp_percentages[0]:.2f}%")
    print(f"Percentage of Pokemon with medium HP: {hp_percentages[1]:.2f}%")
    print(f"Percentage of Pokemon with high HP: {hp_percentages[2]:.2f}%")
  if choice ==  "3":
    result, increase = highest_attack_increase(read_data_file())
    print(f"The Pokemon(s) with the highest increase in attack is/are: {', '.join(result)}")
    print(f"The highest increase is: {increase}")
  if choice == "4":
    result, weight = fattest_pokemon(read_data_file())
    print(f"The Pokémon(s) with the highest weight is/are: {', '.join(result)}")
    print(f"The highest weight is: {weight}")
  if choice == "5":
    print("\n\tThank you for using this program!!")
    exit()
    
#call main this way because its good practice
if __name__ == "__main__":
  main()
