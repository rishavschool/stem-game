import time
import os
from families import *
from locations import locations
from actions_map import actions_map
from helper import *
from equippables import *
from item_stats import item_stats
from colors import TerminalColors

user = None
old_location = None
location = "entrance"
dead = False


def get_family_class(family_name):
  family_classes = {
    "unc": Unc,
    "ravikanth": Ravikanth,
    "potdar": Potdar
  }
  
  return family_classes.get(family_name.lower(), Ravikanth)

def set_location(goal):
  global location
  location = goal

def activate_location_defects():
  global location
  global old_location

  #dementia means 40% of your actions won't go through because you forget
  if "Dementia" in user.defects:
    if chance(25):
      clear_terminal()
      print("You forgot what you are doing because you have dementia")
      location = old_location
      time.sleep(2)


def inventory_options():
  clear_terminal()
  print("Actions:")
  choice = select_from_choices(["Equip hat", "Equip shirt", "Equip pants", "Equip shoes"])

  if choice is None:
    return
  
  clear_terminal()

  #display all items of x category in the users inventory
  choice_to_item = {
    "Equip hat": "hat",
    "Equip shirt": "shirt",
    "Equip pants": "pants",
    "Equip shoes": "shoes"
  }
  category = choice_to_item[choice]

  #check which items are owned by user and store in overlap array
  overlap = [key.capitalize() for key in user.inventory.keys() if key in equippables[category] and user.inventory[key] != 0]
  overlap.append("None")
  new_equip = select_from_choices(overlap)

  if isinstance(new_equip, str):
    new_equip = new_equip.lower()

  currently_equipped = user.equipped[category]

  if new_equip is None:
    return

  #remove the current boost
  if currently_equipped != "none":
    current_boost = item_stats[currently_equipped][0]
    current_boost_category = item_stats[currently_equipped][1]

    current_boost_attribute = getattr(user, current_boost_category)
    setattr(user, current_boost_category, current_boost_attribute - current_boost)

   #add new boost
  if new_equip != "none":
    new_boost = item_stats[new_equip][0]
    new_boost_category = item_stats[new_equip][1]

    new_boost_attribute = getattr(user, new_boost_category)
    setattr(user, new_boost_category, new_boost_attribute + new_boost)

  user.equipped[category] = new_equip


def action_options():
  global location
  print("Actions:")
  if location.lower() in actions_map:
    actions_map[location.lower()](user)
  else:
    clear_terminal()
    print("There are no available actions for this location")
    time.sleep(1)


def movement_options():
  global old_location
  global location
  old_location = location
  print("Locations:")
    
  choices = locations[location.lower()] 
  choice = select_from_choices(choices)
       
  if choice is not None:
    set_location(choice)

def start_game():
  global user
  clear_terminal()
  print("Welcome to the Scum of Stem game.\n")
  name = input("Enter your first name:\n").capitalize()
  family = input("Select a family (Potdar, Unc, Ravikanth):\n").lower()
  user = get_family_class(family)(name)

def frame():
  clear_terminal()
  print(f"{TerminalColors.YELLOW}Disclaimer: Any resemblance to real people, living or dead, in this game is purely coincidental. The characters, events, and scenarios portrayed are entirely fictional.{TerminalColors.RESET}")
  print(user,"\n")
  print(f"You are currently at the {TerminalColors.BLUE}{TerminalColors.BOLD}{TerminalColors.UNDERLINE}{location}{TerminalColors.RESET} of the {TerminalColors.BOLD}Downingtown Stem Academy{TerminalColors.RESET}\n")
  print("Options:")
  choice = select_from_choices(["Move", "Action", "Inventory"])
  clear_terminal()

  if choice == "Move":
    movement_options()
    activate_location_defects()
  elif choice == "Action": #action is not yet implemented
    action_options()
  elif choice == "Inventory":
    inventory_options()
  else: #unavailable choice so we re render
    return frame()

  if dead == False: 
    return frame()

start_game()
frame()