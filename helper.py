import random
import math
import os

def sign_as_string(number):
  if number >= 0:
    return "+"
  else:
    return "-"

def random_between(lower: int, higher: int):
  return math.floor(random.random() * higher + lower)

#creates a choice selection from the inputted array of choices
def select_from_choices(choices):
  for i, choice in enumerate(choices, start=1):
    print(f"{i}: {choice}")
    
  print("\nResponse:")
  user_input = input()
    
  if user_input.isdigit():
    index = int(user_input) - 1
    if 0 <= index < len(choices):
      return choices[index]

  return None

    
#returns a true or false value based on the success from the inputted chance percentage
def chance(percent: int):
  if random.random() <= (percent / 100):
    return True
  
  return False

  
#clears the terminal/screen
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')